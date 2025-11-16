// 获取DOM元素
const urlInput = document.getElementById('url-input');
const generateBtn = document.getElementById('generate-btn');
const qrSection = document.getElementById('qr-section');
const qrcodeCanvas = document.getElementById('qrcode');
const downloadBtn = document.getElementById('download-btn');
const clearBtn = document.getElementById('clear-btn');
const errorMessage = document.getElementById('error-message');

// 验证URL格式
function isValidURL(string) {
    try {
        const url = new URL(string);
        return url.protocol === 'http:' || url.protocol === 'https:';
    } catch (_) {
        return false;
    }
}

// 显示错误信息
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    setTimeout(() => {
        errorMessage.style.display = 'none';
    }, 5000);
}

// 隐藏错误信息
function hideError() {
    errorMessage.style.display = 'none';
}

// 生成QR码
function generateQRCode(url) {
    // 隐藏之前的错误信息
    hideError();

    // 验证URL
    if (!url || url.trim() === '') {
        showError('请输入URL地址');
        return;
    }

    // 如果URL没有协议，自动添加https://
    let processedURL = url.trim();
    if (!processedURL.startsWith('http://') && !processedURL.startsWith('https://')) {
        processedURL = 'https://' + processedURL;
    }

    // 验证URL格式
    if (!isValidURL(processedURL)) {
        showError('请输入有效的URL地址（例如：https://example.com）');
        return;
    }

    // 生成QR码
    QRCode.toCanvas(qrcodeCanvas, processedURL, {
        width: 300,
        margin: 2,
        color: {
            dark: '#000000',
            light: '#FFFFFF'
        },
        errorCorrectionLevel: 'M'
    }, function (error) {
        if (error) {
            showError('生成QR码时出错，请重试');
            console.error('QR码生成错误:', error);
        } else {
            // 显示QR码区域
            qrSection.style.display = 'block';
            // 更新下载按钮的URL
            downloadBtn.setAttribute('data-url', processedURL);
        }
    });
}

// 下载QR码
function downloadQRCode() {
    const canvas = qrcodeCanvas;
    const url = canvas.toDataURL('image/png');
    const link = document.createElement('a');
    link.download = 'qrcode.png';
    link.href = url;
    link.click();
}

// 清除QR码
function clearQRCode() {
    qrSection.style.display = 'none';
    urlInput.value = '';
    urlInput.focus();
    hideError();
}

// 事件监听器
generateBtn.addEventListener('click', () => {
    generateQRCode(urlInput.value);
});

// 按Enter键生成QR码
urlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        generateQRCode(urlInput.value);
    }
});

// 下载按钮
downloadBtn.addEventListener('click', downloadQRCode);

// 清除按钮
clearBtn.addEventListener('click', clearQRCode);

// 页面加载时聚焦输入框
window.addEventListener('load', () => {
    urlInput.focus();
});

