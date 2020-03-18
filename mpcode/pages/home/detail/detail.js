// pages/home/detail/detail.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },
	showQrcode() {
		wx.previewImage({
			urls: [
				'https://ossweb-img.qq.com/images/lol/web201310/skin/big10006.jpg',
				'https://ossweb-img.qq.com/images/lol/web201310/skin/big10006.jpg'
			],
			current: 'https://ossweb-img.qq.com/images/lol/web201310/skin/big10006.jpg' // 当前显示图片的http链接      
		})
	},
})