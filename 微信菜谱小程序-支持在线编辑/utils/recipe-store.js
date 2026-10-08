const defaultRecipes = require('../data/recipes')

const CUSTOM_KEY = 'customRecipes'
const EDITS_KEY = 'recipeEdits'

function clone(value) {
  return JSON.parse(JSON.stringify(value))
}

function getRecipes() {
  const edits = wx.getStorageSync(EDITS_KEY) || {}
  const customRecipes = wx.getStorageSync(CUSTOM_KEY) || []
  const builtInRecipes = defaultRecipes.map(recipe => ({ ...clone(recipe), ...(edits[recipe.id] || {}) }))
  return [...builtInRecipes, ...clone(customRecipes)]
}

function getRecipe(id) {
  return getRecipes().find(recipe => recipe.id === id)
}

function saveRecipe(recipe) {
  const savedRecipe = clone(recipe)
  delete savedRecipe.favorite
  const isBuiltIn = defaultRecipes.some(item => item.id === savedRecipe.id)

  if (isBuiltIn) {
    const edits = wx.getStorageSync(EDITS_KEY) || {}
    edits[savedRecipe.id] = savedRecipe
    wx.setStorageSync(EDITS_KEY, edits)
    return savedRecipe
  }

  const customRecipes = wx.getStorageSync(CUSTOM_KEY) || []
  const index = customRecipes.findIndex(item => item.id === savedRecipe.id)
  if (index >= 0) customRecipes[index] = savedRecipe
  else customRecipes.unshift(savedRecipe)
  wx.setStorageSync(CUSTOM_KEY, customRecipes)
  return savedRecipe
}

module.exports = { getRecipes, getRecipe, saveRecipe }
