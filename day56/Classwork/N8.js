function removeSmallest(arr) {
    if (arr.length === 0) return [];

    const minIndex = arr.indexOf(Math.min(...arr));
    return arr.slice(0, minIndex).concat(arr.slice(minIndex + 1));
}
console.log(removeSmallest([1, 2, 3, 4, 5]));
console.log(removeSmallest([5, 3, 2, 1, 4]));
console.log(removeSmallest([2, 2, 1, 2, 1]));
