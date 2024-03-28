# IMPORTANT
If you need to change the addresses of anything (deployed contracts, oracles, etc) -- please do so in `snippets/addresses.mdx`. All usages of these variables will then automatically change across all docs pages.

Similarly, if you're adding a new address or other value into the docs that is going to change relatively often, please also add it as a snippet.


### Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm install
```

Run the following command at the root of your documentation (where mint.json is)

```
npm run dev
```

Run the following to check for broken links (does not check headers and external links):

```
npm run broken-links
```

### Deployment

The `main` branch is automatically deployed to docs.galadriel.com.


#### Troubleshooting

- Mintlify dev isn't running - Run `mintlify install` it'll re-install dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `mint.json`
