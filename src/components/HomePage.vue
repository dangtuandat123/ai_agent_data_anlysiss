<template>
  <div>
    <!-- Enhanced Background Elements -->
    <div class="cyber-bg">
      <div class="cyber-gradient"></div>
      <div class="matrix-rain" id="matrixRain"></div>
    </div>

    <div class="particles" id="particlesContainer"></div>

    <div class="data-streams" id="dataStreams"></div>

    <div class="orb orb1"></div>
    <div class="orb orb2"></div>
    <div class="orb orb3"></div>

    <div class="grid-overlay">
      <div class="grid-lines"></div>
      <div class="grid-glow"></div>
    </div>

    <div class="scanlines"></div>
    <div class="noise-overlay"></div>

    <!-- Navigation -->
    <nav>
      <div class="nav-container">
        <a href="#top" class="logo">DataAnalysis AI</a>
        <ul class="nav-links">
          <li><a href="#features">Features</a></li>
          <li><a href="#pricing">Pricing</a></li>
          <li><a href="#stats">Stats</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
        <div class="nav-bottom">
          <a href="#" class="cyber-button">Dùng ngay</a>
        </div>
        <button class="mobile-menu-button" id="mobileMenuBtn">
          <div class="hamburger">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </button>
      </div>
    </nav>

    <!-- Mobile Menu -->
    <div class="mobile-menu-overlay" id="mobileMenuOverlay"></div>
    <div class="mobile-menu" id="mobileMenu">
      <div class="mobile-menu-header">
        <a href="#top" class="mobile-menu-logo">NexusFlow</a>
        <button class="mobile-menu-close" id="mobileMenuClose">✕</button>
      </div>
      <div class="mobile-menu-cta">
        <a href="#" class="cyber-button">Access Terminal</a>
      </div>
      <nav class="mobile-menu-nav">
        <ul>
          <li><a href="#features">Features</a></li>
          <li><a href="#pricing">Pricing</a></li>
          <li><a href="#stats">Stats</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-container">
        <h1 class="hero-title">
          <span class="hero-nexus">Data Analysis</span><span class="hero-flow">
            AGENT</span>
        </h1>
        <p class="hero-subtitle">Phân tích dữ liệu trở nên dễ dàng hơn với công cụ AI.</p>
        <div class="hero-buttons">
          <router-link to="/chatbot" class="btn-primary">Bắt đầu</router-link>
          <a href="#" class="btn-secondary">View Documentation</a>
        </div>
      </div>
    </section>
    <!-- Stats Section -->
    <section class="stats fade-up" id="stats">
      <div class="stats-container">
        <div class="stats-grid">
          <div class="stat-item">
            <span class="stat-number">50K+</span>
            <span class="stat-label">Active Users</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">99.9%</span>
            <span class="stat-label">Uptime</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">500M+</span>
            <span class="stat-label">Tasks Processed</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">180+</span>
            <span class="stat-label">Countries</span>
          </div>
        </div>
      </div>
    </section>
    <!-- Features Section -->
    <section class="features fade-up" id="features">
      <div class="features-container">
        <div class="section-header">
          <h2 class="section-title">Dùng trong</h2>
          <!-- <p class="section-subtitle">Advanced modules designed for maximum efficiency and seamless integration</p> -->
        </div>

        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">💰</div>
            <h3>Tài chính</h3>
            <p>Phân tích dữ liệu siêu tốc, giúp bạn đưa ra quyết định đầu tư chính xác và quản lý tài sản hiệu quả.</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">📈</div>
            <h3>Marketing</h3>
            <p>Tối ưu hóa chiến lược tiếp thị, tự động hóa các chiến dịch và dự đoán xu hướng thị trường để tăng doanh
              thu.</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">🎓</div>
            <h3>Giáo dục (EDU)</h3>
            <p>Mở rộng không gian học tập với các công cụ tương tác, cá nhân hóa lộ trình học và thúc đẩy sự sáng tạo
              của học sinh.</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Khoa học Dữ liệu</h3>
            <p>Sử dụng các thuật toán mạnh mẽ để khai thác insight từ dữ liệu lớn, giúp doanh nghiệp hiểu rõ hơn về
              khách hàng.</p>
          </div>

          <div class="feature-card">
            <div class="feature-icon">🔬</div>
            <h3>Nghiên cứu</h3>
            <p>Hỗ trợ phân tích, tổng hợp thông tin và mô phỏng các thí nghiệm phức tạp, đẩy nhanh tiến độ các công
              trình khoa học.</p>
          </div>
        </div>

      </div>
    </section>
    <!-- Footer -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-links">
          <a href="#">Privacy Policy</a>
          <span class="footer-separator">•</span>
          <a href="#">Terms of Service</a>
          <span class="footer-separator">•</span>
          <a href="#">Documentation</a>
          <span class="footer-separator">•</span>
          <a href="#">Contact Support</a>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2025 NexusFlow Systems. All realities reserved.</p>
          <p class="footer-credit">Brought to you by <a target="_blank" rel="noopener nofollow">TEMMMM</a></p>
        </div>
      </div>
    </footer>


  </div>
</template>

<script>

export default {

}
</script>

<style scoped></style>
