// 等待DOM和库加载完成
function initApp() {
    // 检查QRCode库是否加载
    if (typeof QRCode === 'undefined') {
        console.error('QRCode库未加载');
        const errorDiv = document.createElement('div');
        errorDiv.style.cssText = 'color: red; padding: 20px; text-align: center; background: #fee; border-radius: 10px; margin: 20px;';
        errorDiv.innerHTML = '<h3>⚠️ QRCode库加载失败</h3><p>请确保 qrcode.js 文件存在</p>';
        document.body.insertBefore(errorDiv, document.body.firstChild);
        return;
    }

    // 获取DOM元素
    const urlInput = document.getElementById('url-input');
    const generateBtn = document.getElementById('generate-btn');
    const qrSection = document.getElementById('qr-section');
    const qrcodeCanvas = document.getElementById('qrcode');
    const downloadBtn = document.getElementById('download-btn');
    const clearBtn = document.getElementById('clear-btn');
    const errorMessage = document.getElementById('error-message');

    // 验证所有元素是否存在
    if (!urlInput || !generateBtn || !qrSection || !qrcodeCanvas) {
        console.error('必要的DOM元素未找到');
        return;
    }

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
        if (errorMessage) {
            errorMessage.textContent = message;
            errorMessage.style.display = 'block';
            setTimeout(() => {
                if (errorMessage) {
                    errorMessage.style.display = 'none';
                }
            }, 5000);
        } else {
            alert(message);
        }
    }

    // 隐藏错误信息
    function hideError() {
        if (errorMessage) {
            errorMessage.style.display = 'none';
        }
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

        // 显示加载状态
        generateBtn.disabled = true;
        generateBtn.textContent = '生成中...';

        // 生成QR码 - 优先使用在线API（更可靠，符合标准）
        // 如果在线API失败，再尝试本地库
        generateQRCodeWithAPI(processedURL);
    }

    // 使用在线API生成QR码（主要方案 - 更可靠）
    function generateQRCodeWithAPI(url) {
        // 尝试多个QR码生成API作为备用
        const apis = [
            'https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=',
            'https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=',
            'https://api.qrserver.com/v1/create-qr-code/?size=300x300&margin=2&data='
        ];
        
        let currentApiIndex = 0;
        
        function tryNextAPI() {
            if (currentApiIndex >= apis.length) {
                // 所有API都失败，尝试本地库
                generateBtn.disabled = false;
                generateBtn.textContent = '生成QR码';
                console.warn('所有在线API都失败，尝试本地库');
                tryLocalLibrary(url);
                return;
            }
            
            const apiUrl = apis[currentApiIndex] + encodeURIComponent(url);
            const img = new Image();
            img.crossOrigin = 'anonymous';
            
            // 设置超时
            const timeout = setTimeout(function() {
                console.warn('API ' + (currentApiIndex + 1) + ' 超时，尝试下一个');
                currentApiIndex++;
                tryNextAPI();
            }, 5000);
            
            img.onload = function() {
                clearTimeout(timeout);
                // 将图片绘制到canvas
                const ctx = qrcodeCanvas.getContext('2d');
                qrcodeCanvas.width = 300;
                qrcodeCanvas.height = 300;
                
                // 填充白色背景
                ctx.fillStyle = '#FFFFFF';
                ctx.fillRect(0, 0, 300, 300);
                
                // 绘制QR码图片
                ctx.drawImage(img, 0, 0, 300, 300);
                
                // 显示QR码区域
                qrSection.style.display = 'block';
                // 更新下载按钮的URL
                if (downloadBtn) {
                    downloadBtn.setAttribute('data-url', url);
                }
                
                // 恢复按钮状态
                generateBtn.disabled = false;
                generateBtn.textContent = '生成QR码';
                
                console.log('使用在线API生成QR码成功 (API ' + (currentApiIndex + 1) + ')');
            };
            
            img.onerror = function() {
                clearTimeout(timeout);
                console.warn('API ' + (currentApiIndex + 1) + ' 失败，尝试下一个');
                currentApiIndex++;
                tryNextAPI();
            };
            
            img.src = apiUrl;
        }
        
        tryNextAPI();
    }
    
    // 使用本地库生成QR码（备用方案）
    function tryLocalLibrary(url) {
        try {
            if (typeof QRCode !== 'undefined' && QRCode.toCanvas) {
                QRCode.toCanvas(qrcodeCanvas, url, {
                    width: 300,
                    margin: 2,
                    color: {
                        dark: '#000000',
                        light: '#FFFFFF'
                    },
                    errorCorrectionLevel: 'M'
                }, function (error) {
                    generateBtn.disabled = false;
                    generateBtn.textContent = '生成QR码';

                    if (error) {
                        showError('生成QR码失败，请检查网络连接后重试');
                        console.error('本地库生成失败:', error);
                    } else {
                        qrSection.style.display = 'block';
                        if (downloadBtn) {
                            downloadBtn.setAttribute('data-url', url);
                        }
                        console.log('使用本地库生成QR码（可能无法扫描，建议使用网络）');
                    }
                });
            } else {
                showError('无法生成QR码，请检查网络连接');
            }
        } catch (error) {
            generateBtn.disabled = false;
            generateBtn.textContent = '生成QR码';
            showError('生成QR码失败：' + error.message);
            console.error('本地库异常:', error);
        }
    }

    // 下载QR码
    function downloadQRCode() {
        try {
            const canvas = qrcodeCanvas;
            const url = canvas.toDataURL('image/png');
            const link = document.createElement('a');
            link.download = 'qrcode.png';
            link.href = url;
            link.click();
        } catch (error) {
            showError('下载失败：' + error.message);
            console.error('下载错误:', error);
        }
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
    if (downloadBtn) {
        downloadBtn.addEventListener('click', downloadQRCode);
    }

    // 清除按钮
    if (clearBtn) {
        clearBtn.addEventListener('click', clearQRCode);
    }

    // 页面加载时聚焦输入框
    urlInput.focus();

    console.log('URL转QR码工具已初始化');
}

// 如果DOM已经加载完成，直接初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    // DOM已经加载完成，直接初始化
    initApp();
}

