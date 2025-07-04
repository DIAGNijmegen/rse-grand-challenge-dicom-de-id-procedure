import json from '@rollup/plugin-json';

export default [
    // ESM build
    {
        input: 'index.js',
        output: {
            file: 'dist/grand-challenge-dicom-de-id-procedure.esm.js',
            format: 'esm'
        },
        plugins: [json()]
    },
    // UMD build
    {
        input: 'index.js',
        output: {
            file: 'dist//grand-challenge-dicom-de-id-procedure.umd.js',
            format: 'umd',
            name: 'GrandChallengeDICOMDeIdProcedure'
        },
        plugins: [json()]
    },

];
