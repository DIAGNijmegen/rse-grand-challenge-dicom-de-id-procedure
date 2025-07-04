import json from '@rollup/plugin-json';
import terser from '@rollup/plugin-terser';

export default [
    // ESM build
    {
        input: 'index.js',
        output: {
            file: 'dist/grand-challenge-dicom-de-id-procedure.esm.min.js',
            format: 'esm',
            sourcemap: true
        },
        plugins: [json(), terser()],

    },
    {
        input: 'index.js',
        output: {
            file: 'dist/grand-challenge-dicom-de-id-procedure.esm.js',
            format: 'esm',
        },
        plugins: [json()]
    },
    // UMD build
    {
        input: 'index.js',
        output: {
            file: 'dist//grand-challenge-dicom-de-id-procedure.umd.min.js',
            format: 'umd',
            name: 'GrandChallengeDICOMDeIdProcedure',
            sourcemap: true,

        },
        plugins: [json(), terser()],
    },
    {
        input: 'index.js',
        output: {
            file: 'dist//grand-challenge-dicom-de-id-procedure.umd.js',
            format: 'umd',
            name: 'GrandChallengeDICOMDeIdProcedure'
        },
        plugins: [json()],
    },
];
