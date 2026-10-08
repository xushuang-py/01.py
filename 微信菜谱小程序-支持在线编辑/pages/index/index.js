const recipeStore = require('../../utils/recipe-store')

Page({
  data: {
    categories: ['全部', '快手菜', '下饭菜', '肉菜', '海鲜', '素食', '汤羹'],
    activeCategory: '全部',
    keyword: '',
    recipes: [],
    filteredRecipes: [],
    featured: {}
  },
  onLoad() {
    this.loadRecipes()
  },
  onShow() {
    this.loadRecipes()
  },
  loadRecipes() {
    const recipes = recipeStore.getRecipes()
    const saved = wx.getStorageSync('recipeFavorites') || {}
    const next = recipes.map(item => ({ ...item, favorite: !!saved[item.id] }))
    this.setData({ recipes: next, featured: next[0] }, this.applyFilters)
  },
  selectCategory(e) {
    this.setData({ activeCategory: e.currentTarget.dataset.category }, this.applyFilters)
  },
  onSearch(e) {
    this.setData({ keyword: e.detail.value }, this.applyFilters)
  },
  clearSearch() {
    this.setData({ keyword: '' }, this.applyFilters)
  },
  applyFilters() {
    const { recipes, activeCategory, keyword } = this.data
    const term = keyword.trim().toLowerCase()
    const filtered = recipes.filter(item => {
      const matchesCategory = activeCategory === '全部' || item.category === activeCategory
      const matchesTerm = !term || `${item.name}${item.shortDesc}${item.category}`.toLowerCase().includes(term)
      return matchesCategory && matchesTerm
    })
    this.setData({ filteredRecipes: filtered })
  },
  openDetail(e) {
    wx.navigateTo({ url: `/pages/detail/detail?id=${e.currentTarget.dataset.id}` })
  },
  openManage() {
    wx.navigateTo({ url: '/pages/manage/manage' })
  },
  addRecipe() {
    wx.navigateTo({ url: '/pages/editor/editor' })
  },
  toggleFavorite(e) {
    const id = e.currentTarget.dataset.id
    const next = this.data.recipes.map(item => item.id === id ? { ...item, favorite: !item.favorite } : item)
    const target = next.find(item => item.id === id)
    const saved = wx.getStorageSync('recipeFavorites') || {}
    target.favorite ? saved[id] = true : delete saved[id]
    wx.setStorageSync('recipeFavorites', saved)
    this.setData({ recipes: next, featured: next[0] }, this.applyFilters)
  }
})
