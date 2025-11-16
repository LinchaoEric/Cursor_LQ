# URL转QR码生成器

一个简单易用的网页工具，可以将任何URL地址快速转换为二维码。

## 功能特点

- ✅ 快速将URL转换为二维码
- ✅ 自动验证URL格式
- ✅ 自动添加https://协议（如果缺失）
- ✅ 支持下载生成的二维码图片
- ✅ 响应式设计，支持移动设备
- ✅ 现代化的UI界面

## 使用方法

1. 打开 `index.html` 文件（可以直接在浏览器中打开）
2. 在输入框中输入或粘贴URL地址
3. 点击"生成QR码"按钮
4. 生成的二维码会显示在页面上
5. 可以点击"下载QR码"保存图片，或点击"清除"重新开始

## 技术栈

- **HTML5** - 页面结构
- **CSS3** - 样式和动画效果
- **JavaScript** - 交互逻辑
- **qrcode.js** - QR码生成库（通过CDN引入）

## 文件结构

```
url_to_qrcode/
├── index.html      # 主页面
├── styles.css      # 样式文件
├── main.js         # JavaScript逻辑
└── README.md       # 项目说明
```

## 使用示例

支持的URL格式：
- `https://example.com`
- `http://example.com`
- `example.com` (会自动添加https://)
- `www.example.com` (会自动添加https://)

## 浏览器兼容性

支持所有现代浏览器：
- Chrome
- Firefox
- Safari
- Edge

## 注意事项

- 需要网络连接（使用CDN加载qrcode.js库）
- 如果需要在离线环境使用，可以下载qrcode.js库到本地

