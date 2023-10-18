function permutator(arr, length) {
    const result = [];

    function permute(currentPermutation, depth) {
        if (depth === length) {
            console.log([...currentPermutation]);
            result.push([...currentPermutation]);
            return;
        }

        for (let i = 0; i < arr.length; i++) {
            currentPermutation.push(arr[i]);
            permute(currentPermutation, depth + 1);
            currentPermutation.pop();
        }
    }

    permute([], 0);
    return result;
}

onmessage = function (e) {
    var comps = e.data

    var perm = []
    perm.normal = permutator(comps.normal, 5);
    perm.ancient = permutator(comps.ancient.concat(comps.normal), 9);

    postMessage(true);
};