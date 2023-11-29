# Evensi Culture

The incoming Python Engineer is going to enjoy being part of a tight-knit, battle-tested group of hackers-first at Evensi.

Build incrementally with the group
Learn from each other
Make decisions together

Eat lunch together
Leave together
Leave no person behind: If someone is staying late, but says it's all fine and to go home, then stay late and finish as a team.

## Exercise Daily
### 1. Start by making small changes to your daily routine: if you didn't learning
###    anything before you leave the office, then you are doing something wrong.
### 2. Practice with Beginner mindset: re-learn the basics to understand side effects
###    i.e. React basics of components, props, useState, useEffect, etc. to Python
### 3. Push yourself to solve difficult problems. Walk outside to clear your head.

## Now Build Products
### 1. Always Focus on the Customer
### 2. Always Find Business Value
### 3. Communicate with your Team


# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default {
  // other rules...
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    project: ['./tsconfig.json', './tsconfig.node.json'],
    tsconfigRootDir: __dirname,
  },
}
```

- Replace `plugin:@typescript-eslint/recommended` to `plugin:@typescript-eslint/recommended-type-checked` or `plugin:@typescript-eslint/strict-type-checked`
- Optionally add `plugin:@typescript-eslint/stylistic-type-checked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and add `plugin:react/recommended` & `plugin:react/jsx-runtime` to the `extends` list
