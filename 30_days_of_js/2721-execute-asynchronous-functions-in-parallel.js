/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
const promiseAll = (functions) => {
    return new Promise((resolve, reject) => {
        const results = new Array(functions.length)
        let count = 0

        functions.map((fn, i) => {
            fn()
            .then(val => {
                results[i] = val;
                count += 1;

                if (count === functions.length) {
                    resolve(results);
                }
            })
            .catch(err => reject(err));
        });
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */