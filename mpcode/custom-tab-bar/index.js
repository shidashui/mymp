Component({
  options: {
    addGlobalClass: true,
  },
  data: {
    selected: 0,
    "list": [
      {
        "pagePath": "/pages/index/index",
        "iconPath": "/images/tabbar/index1.png",
        "selectedIconPath": "/images/tabbar/index2.png",
        "text": "首页"
      },
      {
        "pagePath": "/pages/activity/activity",
        "iconPath": "/images/tabbar/cate1.png",
        "selectedIconPath": "/images/tabbar/cate2.png",
        "text": "活动"
      },
      {
        "pagePath": "/pages/tree_hole/tree_hole",
        "iconPath": "/images/tabbar/cart1.png",
        "selectedIconPath": "/images/tabbar/cart2.png",
        "text": "树洞"
      },
      {
        "pagePath": "/pages/my/my",
        "iconPath": "/images/tabbar/my1.png",
        "selectedIconPath": "/images/tabbar/my2.png",
        "text": "我的"
      }
    ]
  },

  methods: {
    switchTab(e) {      
      const url = e.currentTarget.dataset.path
      wx.switchTab({
        url
      })
    }
  },
  pageLifetimes: {
  },
})