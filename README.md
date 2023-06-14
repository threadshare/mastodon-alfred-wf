# mastodon-alfred-wf
---

# Mastodon Toot Alfred Workflow

此项目是一个用于 Alfred 的 Workflow，允许用户直接通过 Alfred 发布新的嘟嘟到自建的 Mastodon 实例。

## 安装

1. 下载最新版本的 `.alfredworkflow` 文件。
2. 双击 `.alfredworkflow` 文件，它将会自动安装到 Alfred 中。

## 配置

1. 在 Alfred 中，找到 Mastodon Toot Workflow，点击右上角的 `[x]` 按钮进入 Workflow 的设置。
2. 在 "Variables" 选项卡中，填入你的 Mastodon 实例的访问令牌 (`MASTODON_TOKEN`) 和实例 URL (`MASTODON_URL`)。

## 使用

在 Alfred 中输入以下命令来发布一条新的嘟嘟：

```
md 这是一条消息
```

其中 "md" 是触发此 Workflow 的关键词，"这是一条消息" 是你想发布的嘟嘟的内容。

## 许可

这个项目采用 MIT 许可。查看 [LICENSE](LICENSE) 文件以获取更多信息。

---

以上只是一个简单的 README 文件的模板，你可能需要根据你的项目具体情况进行修改和增补。
