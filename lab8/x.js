/**
 * Created by Jarek on 23.05.15.
 */

var _ = require('./node_modules/lodash')._;

var L = [10, 11, 12, 15, 20, 21, 22, 23, 24, 29];

var trim = function (L, ro) {
    var m = L.length;
    var L1 = [L[0]];
    var last = L[0];
    var i;
    for (i = 1; i < m; i++) {
        if (last < (1 - ro) * L[i]) {
            L1.push(L[i]);
            last = L[i];
        }
    }
    return L1;
};

var mergeList = function (L1, L2) {
    var result = [];
    var il = 0, ir = 0;
    while (il < L1.length && ir < L2.length) {
        if (L1[il] < L2[ir]) {
            result.push(L1[il++]);
        } else {
            result.push(L2[ir++]);
        }
    }
    return result.concat(L1.slice(il).concat(L2.slice(ir)));
};

var increaseList = function (L, value) {
    var result = [];
    _.each(L, function (entry, index) {
        entry = entry + value;
        result.push(entry);
    });
    return result;
};

//console.log(trim([1, 104], 0.05));

var approxSubsetSum = function (S, t, epsilon) {
    var n = S.length;
    var L0 = [[0]];
    var i;
    for (i = 1; i <= n; i++) {

        L0[i] = mergeList(L0[i - 1], increaseList(L0[i - 1], S[i - 1]));
        console.log("====Merge======", L0[i]);
        L0[i] = trim(L0[i], 0.05);
        console.log("=====TRIM=====", L0[i]);
        _.remove(L0[i], function (n) {
            return n > t;
        });
        console.log("====Remove=====", L0[i]);
        console.log("\n");
    }
    return L0[n];
};

console.log(approxSubsetSum([104, 102, 201, 101], 308, 0.20));