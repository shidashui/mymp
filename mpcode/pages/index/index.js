const title_dict = {'home':'话题', 'activity':'活动', 'my':'我的'}

Page({
  data: {
		title:'话题',
    PageCur: 'home'
  },
  NavChange(e) {
		let cur = e.currentTarget.dataset.cur
    this.setData({
      PageCur: cur,
			title: title_dict[cur]
    })
  },
  onShareAppMessage() {
    return {
      title: 'ColorUI-高颜值的小程序UI组件库',
      imageUrl: '/images/share.jpg',
      path: '/pages/index/index'
    }
  },
	/**
	 * 生命周期函数--监听页面加载
	 */
	onLoad: function (options) {
	},
})