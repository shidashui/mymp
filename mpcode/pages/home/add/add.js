// pages/home/add/add.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
		imgList: [],
		textareaBValue: ''
  },
	formSubmit: function (e) {
	    console.log('form发生了submit事件，携带数据为：', e.detail.value)
	},
	ChooseImage() {
	    wx.chooseImage({
	      count: 9, //默认9
	      sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
	      sourceType: ['album'], //从相册选择
	      success: (res) => {
	        if (this.data.imgList.length != 0) {
	          this.setData({
	            imgList: this.data.imgList.concat(res.tempFilePaths)
	          })
	        } else {
	          this.setData({
	            imgList: res.tempFilePaths
	          })
	        }
	      }
	    });
	  },
	ViewImage(e) {
		wx.previewImage({
			urls: this.data.imgList,
			current: e.currentTarget.dataset.url
		});
	},
	DelImg(e) {
		wx.showModal({
			title: '召唤师',
			content: '确定要删除这段回忆吗？',
			cancelText: '再看看',
			confirmText: '再见',
			success: res => {
				if (res.confirm) {
					this.data.imgList.splice(e.currentTarget.dataset.index, 1);
					this.setData({
						imgList: this.data.imgList
					})
				}
			}
		})
	},
	textareaBInput(e) {
	    this.setData({
	      textareaBValue: e.detail.value
	    })
	  },
})