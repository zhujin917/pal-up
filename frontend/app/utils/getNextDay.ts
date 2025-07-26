const monthDict = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"];
const dayDict = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];

class Day {
    timestamp: number;
    year: number;
    month: string | undefined;
    date: number;
    day: string | undefined;
    beStr: string;
    displayStr: string;
    constructor(timestamp: number) {
        this.timestamp = timestamp;
        const date = new Date(timestamp);
        this.year = date.getFullYear();
        this.month = monthDict[date.getMonth()];
        this.date = date.getDate();
        this.day = dayDict[date.getDay()];
        this.beStr = `${this.year}-${date.getMonth() + 1}-${this.date}`;
        this.displayStr = `${this.month}${this.date}日 ${this.day}`;
    }
}

export default function (n: number) {
    let timestamp = Date.now();
    const result: Array<Day> = [new Day(timestamp)];
    for (let i = 0; i < n; i += 1) {
        timestamp += 86400000;
        result.push(new Day(timestamp));
    }
    return result;
}