module.exports = {
    purge: {
        enabled: true,
        content: [
            "./index.html",
            "./src/**/*.js",
            "./src/**/*.jsx",
            "./src/**/*.vue",
        ],
    },
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {},
    },
    variants: {
        extend: {},
    },
    plugins: [],
}