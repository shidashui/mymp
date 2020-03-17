const app = getApp();

Component({
  options: {
    addGlobalClass: true,
  },
  data: {
		StatusBar: app.globalData.StatusBar,
		CustomBar: app.globalData.CustomBar,
  },
	methods:{
		//跳到详情页
		toDetail(e){
			console.log('跳转')
			wx.navigateTo({
				url:'../activity/detail/detail',
			})
		}
	}
})
