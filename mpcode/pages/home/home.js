const app = getApp();

Component({
  options: {
    addGlobalClass: true,
  },
  data: {
		StatusBar: app.globalData.StatusBar,
		CustomBar: app.globalData.CustomBar,
    TabCur: 0,
		tabNav:['全部','最新','热点'],
		scrollLeft:0
  },
	methods:{
		tabSelect: function(e) {
			this.setData({
				TabCur: e.currentTarget.dataset.id,
				scrollLeft: (e.currentTarget.dataset.id-1)*60
			})
		}
	}
})
