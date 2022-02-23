## About Notion2Medium

[![PyPI version](https://badge.fury.io/py/notion2medium.svg)](https://badge.fury.io/py/notion2medium)
[![Code Quality](https://github.com/echo724/notion2medium/actions/workflows/code_quality.yaml/badge.svg)](https://github.com/echo724/notion2medium/actions/workflows/code_quality.yaml)

- Publish a post to **Medium** just from your **Notion Page** by **Console Cli**

## API Keys(Token)

- **Notion API Token**: create [an integration and find the token](https://www.notion.so/my-integrations). → [Learn more about authorization](https://developers.notion.com/docs/authorization).

- **Medium API Token**: create **Medium Integration** from [Medium Setting](https://medium.com/me/settings)

- Then save your api key(token) as your os **environment variable**

```Bash
$ export NOTION_TOKEN="{your integration token key}"

$ export MEDIUM_TOKEN="{your integration token key}"
```

- Or add these commands to your shell config files(`.bashrc` or `.zshrc`)

## Install

```Bash
$ pip install notion2medium
```

## `Select` Command

- Retrieves **Notion Page** list from **Notion Database**.

- Ask user titles of Notion pages and will call `publish` command to publish the selected page.

- `select` commands require either `id` or `url` of the Notion Database or Page.

```Bash
$ notion2medium select -i <Notion Database id>
```
## `Publish` Command

- Publishes a Medium Post from **Notion Page**.

- Retrieves Notion Page's content(children blocks) as markdown and Page's tags.

- `select` commands require either `id` or `url` of the Notion Database or Page.

```Bash
$ notion2medium select -i <Notion Database id>
```
## To-do

- [x] Download file object(image and files)
- [x] Table blocks
- [x] Synced Block
- [ ] Page Exporter
- [ ] Database Exporter
- [ ] Child page
- [ ] Column List and Column Blocks

## Contribution

Please read [Contribution Guide](CONTRIBUTION.md)

## Donation

If you think **Notion2Md** is helpful to you, you can support me here:

<a href="https://www.buymeacoffee.com/echo724" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 54px;" height="54"></a>

## License
[MIT](https://choosealicense.com/licenses/mit/)
