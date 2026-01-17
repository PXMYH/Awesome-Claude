---
layout: default
title: Categories
description: Browse Claude skills by category
---

<div class="categories-page">
  <h1>Categories</h1>
  <p>Browse skills organized by category</p>

  <div class="categories-grid">
    {% for category in site.data.categories %}
    {% assign cat_skills = site.skills | where: "category", category.slug %}
    <a href="{{ '/categories/' | append: category.slug | append: '/' | relative_url }}" class="category-card">
      <h2>{{ category.name }}</h2>
      <p>{{ category.description }}</p>
      <span class="skill-count">{{ cat_skills.size }} skills</span>
    </a>
    {% endfor %}
  </div>
</div>

<style>
.categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}
.category-card {
  display: block;
  padding: 1.5rem;
  background: var(--bg-secondary);
  border-radius: 12px;
  text-decoration: none;
  color: var(--text-color);
  transition: transform 0.2s, box-shadow 0.2s;
}
.category-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.category-card h2 { font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--primary-color); }
.category-card p { color: var(--text-muted); font-size: 0.875rem; margin-bottom: 1rem; }
.skill-count { font-size: 0.75rem; background: var(--primary-color); color: white; padding: 0.25rem 0.5rem; border-radius: 4px; }
</style>
