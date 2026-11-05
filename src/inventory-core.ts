/** 库存 Demo 纯业务逻辑；不依赖浏览器，可直接自动化测试。 */
export interface Item {sku:string;name:string;category:string;price:number;quantity:number;threshold:number}
export const HEADER=['sku','name','category','price','quantity','threshold'] as const;
const maxText={sku:40,name:80,category:40};
export function validateItem(value: unknown): Item {
  if(!value || typeof value!=='object')throw new Error('商品数据不能为空');
  const v=value as Record<string,unknown>;
  for(const k of ['sku','name','category'] as const){if(typeof v[k]!=='string'||!v[k].trim()||v[k].trim().length>maxText[k])throw new Error(`${k} 长度或内容无效`)}
  if(typeof v.price!=='number'||!Number.isFinite(v.price)||v.price<0||Math.round(v.price*100)!==v.price*100)throw new Error('价格必须为非负且最多两位小数');
  for(const k of ['quantity','threshold'] as const){if(typeof v[k]!=='number'||!Number.isSafeInteger(v[k])||v[k]<0)throw new Error(`${k} 必须为非负整数`)}
  return {sku:(v.sku as string).trim(),name:(v.name as string).trim(),category:(v.category as string).trim(),price:v.price as number,quantity:v.quantity as number,threshold:v.threshold as number};
}
export function validateCollection(input:unknown,limit=1000):Item[]{
  if(!Array.isArray(input)||input.length>limit)throw new Error(`商品数量不能超过 ${limit}`);
  const items=input.map(validateItem),ids=new Set<string>();
  for(const item of items){if(ids.has(item.sku))throw new Error(`SKU 重复：${item.sku}`);ids.add(item.sku)}
  return items;
}
export function stats(items:readonly Item[]){return {total:items.length,stock:items.reduce((n,x)=>n+x.quantity,0),low:items.filter(x=>x.quantity<=x.threshold).length}}
export function csvEscape(value:unknown){const s=String(value);return /[",\r\n]/.test(s)?`"${s.replace(/"/g,'""')}"`:s}
export function parseCsv(text:string):string[][]{
  // 显式状态机：避免吞掉非法引号，也支持逗号/引号/换行。
  const result:string[][]=[];let row:string[]=[],field='',quoted=false,closed=false;
  const pushRow=()=>{row.push(field);if(row.some(x=>x!==''))result.push(row);row=[];field='';closed=false};
  for(let i=0;i<text.length;i++){
    const c=text[i];
    if(quoted){if(c==='"'){if(text[i+1]==='"'){field+='"';i++}else{quoted=false;closed=true}}else field+=c;continue}
    if(c==='"'){if(field!==''||closed)throw new Error('CSV 引号格式错误');quoted=true;continue}
    if(c===','){row.push(field);field='';closed=false;continue}
    if(c==='\n'||c==='\r'){if(c==='\r'&&text[i+1]==='\n')i++;pushRow();continue}
    if(closed)throw new Error('CSV 结束引号后包含无效字符');
    field+=c;
  }
  if(quoted)throw new Error('CSV 引号未闭合');
  pushRow();return result;
}
export function importItems(csv:string):Item[]{
  const rows=parseCsv(csv.replace(/^\ufeff/,''));
  if(!rows.length||rows[0].length!==HEADER.length||HEADER.some((x,i)=>rows[0][i]!==x))throw new Error('CSV 表头必须是 '+HEADER.join(','));
  return validateCollection(rows.slice(1).map((row,i)=>{
    if(row.length!==6)throw new Error(`第 ${i+2} 行的列数错误`);
    for(const j of [3,4,5])if(!/^\d+(?:\.\d+)?$/.test(row[j]))throw new Error(`第 ${i+2} 行的数字字段无效`);
    return {sku:row[0],name:row[1],category:row[2],price:Number(row[3]),quantity:Number(row[4]),threshold:Number(row[5])};
  }));
}
export function exportItems(items:readonly Item[]):string{
  const safe=validateCollection([...items]);
  return [HEADER.join(','),...safe.map(x=>HEADER.map(k=>csvEscape(x[k])).join(','))].join('\r\n');
}
