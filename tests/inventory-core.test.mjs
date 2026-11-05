import test from 'node:test';
import assert from 'node:assert/strict';
import { validateItem,validateCollection,stats,parseCsv,importItems,exportItems } from '../dist/inventory-core.js';
const a={sku:'A1',name:'鼠标',category:'电子',price:29.9,quantity:2,threshold:3};
test('库存校验和统计',()=>{
 assert.deepEqual(validateItem(a),a);
 assert.deepEqual(stats([a,{...a,sku:'A2',quantity:8}]),{total:2,stock:10,low:1});
 assert.throws(()=>validateItem({...a,quantity:-1}));
 assert.throws(()=>validateItem({...a,price:NaN}));
 assert.throws(()=>validateCollection([a,a]),/SKU 重复/);
});
test('CSV 双引号及多行解析',()=>{
 const rows=parseCsv('a,b\r\n"hello,world","two""quotes"\r\n"multi\nline",3');
 assert.deepEqual(rows,[['a','b'],['hello,world','two"quotes'],['multi\nline','3']]);
 assert.throws(()=>parseCsv('x,"unclosed'),/引号/);
 assert.throws(()=>parseCsv('x,"a"broken'),/结束引号/);
});
test('CSV 导入与导出往返、BOM、空表',()=>{
 const c=exportItems([a,{...a,sku:'B2',name:'帽子, "蓝"'}]);
 assert.deepEqual(importItems('\ufeff'+c),[a,{...a,sku:'B2',name:'帽子, "蓝"'}]);
 assert.deepEqual(importItems('sku,name,category,price,quantity,threshold\n'),[]);
});
test('CSV 排除重复 SKU、非法数字和错误列数',()=>{
 const header='sku,name,category,price,quantity,threshold\n';
 assert.throws(()=>importItems(header+'x,A,B,1,2,3\nx,C,B,1,2,3'),/重复/);
 assert.throws(()=>importItems(header+'x,A,B,1,2.5,3'),/非负整数/);
 assert.throws(()=>importItems(header+'x,A,B,1,2'),/列数/);
 assert.throws(()=>importItems('name,sku\nA,x'),/表头/);
});
