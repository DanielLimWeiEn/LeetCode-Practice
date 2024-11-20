function maxProfit(prices: number[]): number {
    let currentMin: number = prices[0];
    let result: number = 0;

    for (let i = 0; i < prices.length; i++) {
        currentMin = Math.min(currentMin, prices[i]);

        result = Math.max(result, prices[i] - currentMin);
    }
    return result;
};
