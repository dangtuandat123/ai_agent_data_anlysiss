<template>
  <div class="md-content" v-html="sanitizedMessage"></div>
  </template>

<script>
import { marked } from 'marked';
import DOMPurify from 'dompurify';
import hljs from 'highlight.js';
import 'highlight.js/styles/github.css';

export default {
  props: ['message'],
  computed: {
    sanitizedMessage() {
      // Configure marked to highlight code blocks
      marked.setOptions({
        breaks: true,
        highlight(code, lang) {
          try {
            if (lang && hljs.getLanguage(lang)) {
              return hljs.highlight(code, { language: lang }).value;
            }
            return hljs.highlightAuto(code).value;
          } catch (_) {
            return code;
          }
        }
      });

      const dirty = marked.parse(this.message || '');
      const clean = DOMPurify.sanitize(dirty, { ADD_ATTR: ['target', 'rel'] });

      // Ensure links open in new tab with safe rel
      const wrapper = document.createElement('div');
      wrapper.innerHTML = clean;
      const links = wrapper.querySelectorAll('a');
      links.forEach(a => {
        a.setAttribute('target', '_blank');
        a.setAttribute('rel', 'noopener noreferrer');
      });
      return wrapper.innerHTML;
    }
  }
};
</script>

<style scoped>
/* Markdown content styling to match UI kit */
.md-content { color: #1f2937; font-size: 0.9375rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word; }
.md-content p { margin: 0 0 0.5rem 0; }
.md-content h1, .md-content h2, .md-content h3, .md-content h4 { margin: 0.75rem 0 0.5rem; font-weight: 600; color: #0f172a; }
.md-content ul, .md-content ol { padding-left: 1.25rem; margin: 0.5rem 0; }
.md-content li { margin: 0.25rem 0; }
.md-content a { color: #2563eb; text-decoration: underline; }
.md-content code { background: #e5e7eb; color: #111827; padding: 0.125rem 0.375rem; border-radius: 0.375rem; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 0.875em; }
.md-content pre { background: #0f172a; color: #e5e7eb; padding: 0.75rem; border-radius: 0.5rem; overflow-x: auto; line-height: 1.5; }
.md-content pre code { background: transparent !important; color: inherit; padding: 0; }
.md-content blockquote { border-left: 3px solid #cbd5e1; padding-left: 0.75rem; color: #334155; margin: 0.5rem 0; }
.md-content table { width: 100%; border-collapse: collapse; margin: 0.5rem 0; }
.md-content th, .md-content td { border: 1px solid #e5e7eb; padding: 0.5rem 0.75rem; text-align: left; }
.md-content thead th { background: #f1f5f9; color: #334155; }
.md-content img { max-width: 100%; height: auto; border-radius: 0.5rem; border: 1px solid #e5e7eb; }
</style>
