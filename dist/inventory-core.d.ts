/** 库存 Demo 纯业务逻辑；不依赖浏览器，可直接自动化测试。 */
export interface Item {
    sku: string;
    name: string;
    category: string;
    price: number;
    quantity: number;
    threshold: number;
}
export declare const HEADER: readonly ["sku", "name", "category", "price", "quantity", "threshold"];
export declare function validateItem(value: unknown): Item;
export declare function validateCollection(input: unknown, limit?: number): Item[];
export declare function stats(items: readonly Item[]): {
    total: number;
    stock: number;
    low: number;
};
export declare function csvEscape(value: unknown): string;
export declare function parseCsv(text: string): string[][];
export declare function importItems(csv: string): Item[];
export declare function exportItems(items: readonly Item[]): string;
