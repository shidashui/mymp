const title_dict = {'home':'首页', 'activity':'活动', 'tree_hole':'树洞', 'my':'我的', 'add':'发布'}

Page({
  data: {
		title:'首页',
    PageCur: 'my'
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