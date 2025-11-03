import os

# Enhanced page content with better structure and information
pages = {
    "education": {
        "title": "Education",
        "subtitle": "Academic Journey & Achievements",
        "content": """
        <div class="content-card" data-aos="fade-up">
            <div class="card-icon">
                <i class="fas fa-graduation-cap"></i>
            </div>
            <h3>Harvard Law School</h3>
            <p class="degree"><strong>Juris Doctor (J.D.) - Class of 2024</strong></p>
            <p class="highlight">🏆 Recipient of the Dean's Award for Community Leadership</p>
            <div class="achievements">
                <p><i class="fas fa-check-circle"></i> Editor, Harvard Business Law Review</p>
                <p><i class="fas fa-check-circle"></i> Harvard Association for Law & Business</p>
                <p><i class="fas fa-check-circle"></i> J.D. Admissions Fellow Program</p>
                <p><i class="fas fa-check-circle"></i> Committee For Sports & Entertainment Law</p>
                <p><i class="fas fa-check-circle"></i> Research Focus: IP/Copyright Law in Fashion Industry</p>
            </div>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="100">
            <div class="card-icon">
                <i class="fas fa-university"></i>
            </div>
            <h3>University of California, Los Angeles (UCLA)</h3>
            <p class="degree"><strong>Bachelor of Arts in Psychology - 2020</strong></p>
            <p class="highlight">🎓 Graduated with Distinction in Psychology</p>
            <p>Developed strong analytical and research skills that continue to inform legal work and client relations.</p>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="200">
            <div class="card-icon">
                <i class="fas fa-school"></i>
            </div>
            <h3>Norco College</h3>
            <p class="degree"><strong>Associate of Arts Degrees (3)</strong></p>
            <p>Completed multiple AA degrees demonstrating academic versatility and commitment to education before transferring to UCLA.</p>
        </div>
        """
    },
    "skills": {
        "title": "Skills & Expertise",
        "subtitle": "Professional Competencies & Legal Specializations",
        "content": """
        <div class="skills-grid">
            <div class="content-card skill-card" data-aos="fade-up">
                <div class="card-icon">
                    <i class="fas fa-balance-scale"></i>
                </div>
                <h3>Legal Expertise</h3>
                <div class="skill-list">
                    <div class="skill-item">
                        <i class="fas fa-gavel"></i>
                        <span>Constitutional Law & Religious Freedom</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-copyright"></i>
                        <span>Intellectual Property & Copyright Law</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-briefcase"></i>
                        <span>Commercial Litigation</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-building"></i>
                        <span>Corporate Law & Business Transactions</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-trophy"></i>
                        <span>Sports & Entertainment Law</span>
                    </div>
                </div>
            </div>
            
            <div class="content-card skill-card" data-aos="fade-up" data-aos-delay="100">
                <div class="card-icon">
                    <i class="fas fa-briefcase"></i>
                </div>
                <h3>Professional Experience</h3>
                <div class="skill-list">
                    <div class="skill-item">
                        <i class="fas fa-landmark"></i>
                        <span>Supreme Court of Pakistan - Clerk to Justice Shah</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-city"></i>
                        <span>Corporate Law Firm - New York City Summer Associate</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-scales-balanced"></i>
                        <span>Commercial Litigation - Los Angeles Summer Clerk</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-handshake"></i>
                        <span>Client Relations - Louis Vuitton Beverly Hills</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-cross"></i>
                        <span>Harvard Religious Freedom Clinic - Visiting Fellow</span>
                    </div>
                </div>
            </div>
            
            <div class="content-card skill-card" data-aos="fade-up" data-aos-delay="200">
                <div class="card-icon">
                    <i class="fas fa-pen-fancy"></i>
                </div>
                <h3>Research & Writing</h3>
                <div class="skill-list">
                    <div class="skill-item">
                        <i class="fas fa-search"></i>
                        <span>Advanced Legal Research & Analysis</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-book-open"></i>
                        <span>Scholarly Publications & Editorial Work</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-edit"></i>
                        <span>Legal Writing & Brief Preparation</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-tshirt"></i>
                        <span>IP/Copyright Research in Fashion Industry</span>
                    </div>
                    <div class="skill-item">
                        <i class="fas fa-users"></i>
                        <span>Client Communication & Advocacy</span>
                    </div>
                </div>
            </div>
        </div>
        """
    },
    "books": {
        "title": "Books & Publications",
        "subtitle": "Written Works & Scholarly Contributions",
        "content": """
        <div class="content-card" data-aos="fade-up">
            <div class="card-icon">
                <i class="fas fa-book-open"></i>
            </div>
            <h3>Publications & Written Works</h3>
            <p>As a legal scholar and editor of the Harvard Business Law Review, Saeed Ahmad has contributed to various scholarly publications and legal discourse.</p>
            <p>His research interests include intellectual property law, copyright protection in the fashion industry, constitutional law, and religious freedom.</p>
            <div class="info-box">
                <p><strong>Research Focus Areas:</strong></p>
                <ul>
                    <li>Intellectual Property & Copyright Law</li>
                    <li>Fashion Industry Legal Frameworks</li>
                    <li>Constitutional Rights & Religious Freedom</li>
                    <li>Business Law & Corporate Governance</li>
                </ul>
            </div>
        </div>
        """
    },
    "speaking": {
        "title": "Speaking Engagements",
        "subtitle": "Public Presentations & Panel Discussions",
        "content": """
        <div class="content-card" data-aos="fade-up">
            <div class="card-icon">
                <i class="fas fa-microphone-alt"></i>
            </div>
            <h3>Topics & Expertise</h3>
            <p>Saeed Ahmad is available for speaking engagements on a variety of legal and professional topics.</p>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="100">
            <h3>Speaking Topics Include:</h3>
            <div class="topic-grid">
                <div class="topic-item">
                    <i class="fas fa-praying-hands"></i>
                    <h4>Religious Freedom & Constitutional Law</h4>
                    <p>Insights from work at Harvard's Religious Freedom Clinic</p>
                </div>
                <div class="topic-item">
                    <i class="fas fa-graduation-cap"></i>
                    <h4>Legal Education & Career Development</h4>
                    <p>Journey from community college to Harvard Law School</p>
                </div>
                <div class="topic-item">
                    <i class="fas fa-users"></i>
                    <h4>Diversity in the Legal Profession</h4>
                    <p>Building inclusive legal communities</p>
                </div>
                <div class="topic-item">
                    <i class="fas fa-tshirt"></i>
                    <h4>Intellectual Property in Fashion</h4>
                    <p>Copyright protection and legal frameworks</p>
                </div>
                <div class="topic-item">
                    <i class="fas fa-globe"></i>
                    <h4>Pakistani-American Legal Perspectives</h4>
                    <p>Cross-cultural legal practice and understanding</p>
                </div>
                <div class="topic-item">
                    <i class="fas fa-balance-scale"></i>
                    <h4>International Clerkships</h4>
                    <p>Experience at the Supreme Court of Pakistan</p>
                </div>
            </div>
        </div>
        """
    },
    "interviews": {
        "title": "Media & Interviews",
        "subtitle": "Press Features & Media Appearances",
        "content": """
        <div class="content-card" data-aos="fade-up">
            <div class="card-icon">
                <i class="fas fa-podcast"></i>
            </div>
            <h3>Media Appearances</h3>
            <p>Saeed Ahmad has been featured in various media outlets discussing legal issues, education, career development, and his professional journey from community college to Harvard Law School.</p>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="100">
            <h3>Interview Topics</h3>
            <div class="interview-topics">
                <div class="topic-badge">
                    <i class="fas fa-graduation-cap"></i> Legal Education
                </div>
                <div class="topic-badge">
                    <i class="fas fa-praying-hands"></i> Religious Freedom
                </div>
                <div class="topic-badge">
                    <i class="fas fa-briefcase"></i> Career Development
                </div>
                <div class="topic-badge">
                    <i class="fas fa-landmark"></i> Supreme Court Experience
                </div>
                <div class="topic-badge">
                    <i class="fas fa-copyright"></i> Intellectual Property
                </div>
                <div class="topic-badge">
                    <i class="fas fa-users"></i> Diversity in Law
                </div>
            </div>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="200">
            <h3>Media Inquiries</h3>
            <p>For interview requests or media inquiries, please contact via the <a href="/contact/">contact page</a>.</p>
        </div>
        """
    },
    "portfolio": {
        "title": "Professional Portfolio",
        "subtitle": "Experience & Notable Work",
        "content": """
        <div class="timeline">
            <div class="content-card timeline-item" data-aos="fade-up">
                <div class="timeline-marker"></div>
                <div class="card-icon">
                    <i class="fas fa-cross"></i>
                </div>
                <h3>Harvard Law School Religious Freedom Clinic</h3>
                <p class="position">Visiting Fellow</p>
                <p class="period">Current Position</p>
                <p>Working on constitutional law cases involving religious freedom and First Amendment rights. Conducting legal research and assisting with client representation.</p>
            </div>
            
            <div class="content-card timeline-item" data-aos="fade-up" data-aos-delay="100">
                <div class="timeline-marker"></div>
                <div class="card-icon">
                    <i class="fas fa-landmark"></i>
                </div>
                <h3>Supreme Court of Pakistan</h3>
                <p class="position">Clerk to Justice Shah</p>
                <p class="period">Summer Position</p>
                <p>Assisted in reviewing cases, conducting legal research, and drafting judicial opinions. Gained invaluable insight into international judiciary operations and constitutional law.</p>
            </div>
            
            <div class="content-card timeline-item" data-aos="fade-up" data-aos-delay="200">
                <div class="timeline-marker"></div>
                <div class="card-icon">
                    <i class="fas fa-building"></i>
                </div>
                <h3>Corporate Law Firm, New York City</h3>
                <p class="position">Summer Associate</p>
                <p class="period">Summer Program</p>
                <p>Worked on corporate transactions, mergers and acquisitions, and commercial contracts. Collaborated with partners on high-profile business deals.</p>
            </div>
            
            <div class="content-card timeline-item" data-aos="fade-up" data-aos-delay="300">
                <div class="timeline-marker"></div>
                <div class="card-icon">
                    <i class="fas fa-gavel"></i>
                </div>
                <h3>Commercial Litigation Firm, Los Angeles</h3>
                <p class="position">Summer Clerk</p>
                <p class="period">Summer Program</p>
                <p>Assisted with litigation cases, legal research, and brief preparation. Gained experience in courtroom procedures and client advocacy.</p>
            </div>
            
            <div class="content-card timeline-item" data-aos="fade-up" data-aos-delay="400">
                <div class="timeline-marker"></div>
                <div class="card-icon">
                    <i class="fas fa-gem"></i>
                </div>
                <h3>Louis Vuitton, Beverly Hills</h3>
                <p class="position">Client Advisor - Flagship Store on Rodeo Drive</p>
                <p class="period">Professional Experience</p>
                <p>Developed exceptional client relations and luxury retail skills. Worked with high-profile clientele, enhancing interpersonal and communication abilities.</p>
            </div>
        </div>
        """
    },
    "press": {
        "title": "Press & Media",
        "subtitle": "Media Coverage & Public Recognition",
        "content": """
        <div class="content-card" data-aos="fade-up">
            <div class="card-icon">
                <i class="fas fa-newspaper"></i>
            </div>
            <h3>Press Coverage</h3>
            <p>Saeed Ahmad has been featured in various publications and media outlets for his academic achievements, professional work, and contributions to legal discourse.</p>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="100">
            <h3>Recognition & Features</h3>
            <div class="press-highlights">
                <div class="press-item">
                    <i class="fas fa-trophy"></i>
                    <div>
                        <h4>Dean's Award for Community Leadership</h4>
                        <p>Harvard Law School recognition for outstanding service</p>
                    </div>
                </div>
                <div class="press-item">
                    <i class="fas fa-book"></i>
                    <div>
                        <h4>Harvard Business Law Review</h4>
                        <p>Editor position and scholarly contributions</p>
                    </div>
                </div>
                <div class="press-item">
                    <i class="fas fa-university"></i>
                    <div>
                        <h4>Educational Journey</h4>
                        <p>Featured for path from community college to Harvard Law</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="200">
            <h3>Media Contact</h3>
            <p>For press inquiries or interview requests, please reach out via the <a href="/contact/">contact page</a>.</p>
        </div>
        """
    },
    "contact": {
        "title": "Get in Touch",
        "subtitle": "Contact Information & Connect",
        "content": """
        <div class="contact-grid">
            <div class="content-card contact-card" data-aos="fade-up">
                <div class="card-icon">
                    <i class="fas fa-envelope"></i>
                </div>
                <h3>Email</h3>
                <p class="contact-detail">
                    <a href="mailto:saeed@saeedahmad.com">saeed@saeedahmad.com</a>
                </p>
                <p>Feel free to reach out for inquiries, collaborations, or speaking engagements.</p>
            </div>
            
            <div class="content-card contact-card" data-aos="fade-up" data-aos-delay="100">
                <div class="card-icon">
                    <i class="fas fa-map-marker-alt"></i>
                </div>
                <h3>Location</h3>
                <p class="contact-detail">Cambridge, MA</p>
                <p>Harvard Law School Religious Freedom Clinic</p>
            </div>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="200">
            <h3>Connect on Social Media</h3>
            <div class="social-links-large">
                <a href="https://www.linkedin.com/in/saeedahmad-" target="_blank" class="social-link linkedin">
                    <i class="fab fa-linkedin"></i>
                    <span>LinkedIn</span>
                </a>
                <a href="https://twitter.com/_saeedahmad" target="_blank" class="social-link twitter">
                    <i class="fab fa-twitter"></i>
                    <span>Twitter</span>
                </a>
                <a href="https://www.instagram.com/_saeedahmad/" target="_blank" class="social-link instagram">
                    <i class="fab fa-instagram"></i>
                    <span>Instagram</span>
                </a>
                <a href="https://www.facebook.com/saeedahmaducla" target="_blank" class="social-link facebook">
                    <i class="fab fa-facebook"></i>
                    <span>Facebook</span>
                </a>
            </div>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="300">
            <h3>Professional Inquiries</h3>
            <p>For consulting services, speaking engagements, or legal consultations, please email with details about your inquiry.</p>
            <div class="cta-buttons">
                <a href="/consulting/" class="btn btn-primary">
                    <i class="fas fa-handshake"></i> Consulting Services
                </a>
                <a href="/book-now/" class="btn btn-secondary">
                    <i class="fas fa-calendar"></i> Schedule Meeting
                </a>
            </div>
        </div>
        """
    },
    "consulting": {
        "title": "Legal Consulting",
        "subtitle": "Professional Services & Expertise",
        "content": """
        <div class="content-card" data-aos="fade-up">
            <div class="card-icon">
                <i class="fas fa-handshake"></i>
            </div>
            <h3>Consulting Services</h3>
            <p>Drawing on experience from Harvard Law School, the Supreme Court of Pakistan, and prestigious law firms, Saeed Ahmad offers consulting services in various legal areas.</p>
        </div>
        
        <div class="services-grid">
            <div class="content-card service-card" data-aos="fade-up" data-aos-delay="100">
                <div class="service-icon">
                    <i class="fas fa-praying-hands"></i>
                </div>
                <h3>Religious Freedom & Constitutional Law</h3>
                <p>Expert guidance on First Amendment issues, religious liberty cases, and constitutional rights.</p>
            </div>
            
            <div class="content-card service-card" data-aos="fade-up" data-aos-delay="200">
                <div class="service-icon">
                    <i class="fas fa-copyright"></i>
                </div>
                <h3>Intellectual Property</h3>
                <p>Copyright protection, trademark issues, and IP strategy, particularly in the fashion industry.</p>
            </div>
            
            <div class="content-card service-card" data-aos="fade-up" data-aos-delay="300">
                <div class="service-icon">
                    <i class="fas fa-briefcase"></i>
                </div>
                <h3>Corporate & Business Law</h3>
                <p>Business transactions, corporate governance, and commercial contract review.</p>
            </div>
            
            <div class="content-card service-card" data-aos="fade-up" data-aos-delay="400">
                <div class="service-icon">
                    <i class="fas fa-users"></i>
                </div>
                <h3>Diversity & Inclusion</h3>
                <p>Consulting on building diverse legal teams and inclusive workplace cultures.</p>
            </div>
        </div>
        
        <div class="content-card cta-card" data-aos="fade-up" data-aos-delay="500">
            <h3>Schedule a Consultation</h3>
            <p>To discuss your legal needs and explore how we can work together, please reach out via email or schedule a meeting.</p>
            <div class="cta-buttons">
                <a href="mailto:saeed@saeedahmad.com" class="btn btn-primary">
                    <i class="fas fa-envelope"></i> Email
                </a>
                <a href="/book-now/" class="btn btn-secondary">
                    <i class="fas fa-calendar"></i> Book Consultation
                </a>
            </div>
        </div>
        """
    },
    "book-now": {
        "title": "Schedule a Meeting",
        "subtitle": "Book a Consultation or Speaking Engagement",
        "content": """
        <div class="content-card" data-aos="fade-up">
            <div class="card-icon">
                <i class="fas fa-calendar-check"></i>
            </div>
            <h3>Schedule a Meeting</h3>
            <p>To schedule a consultation, speaking engagement, or professional meeting, please contact Saeed Ahmad via email with your preferred dates and meeting purpose.</p>
        </div>
        
        <div class="booking-grid">
            <div class="content-card booking-card" data-aos="fade-up" data-aos-delay="100">
                <div class="card-icon">
                    <i class="fas fa-handshake"></i>
                </div>
                <h3>Consultation Requests</h3>
                <p>Legal consultations on constitutional law, intellectual property, corporate matters, and religious freedom issues.</p>
                <ul>
                    <li>Initial consultation</li>
                    <li>Ongoing legal guidance</li>
                    <li>Case review and strategy</li>
                </ul>
            </div>
            
            <div class="content-card booking-card" data-aos="fade-up" data-aos-delay="200">
                <div class="card-icon">
                    <i class="fas fa-microphone"></i>
                </div>
                <h3>Speaking Engagements</h3>
                <p>Available for conferences, panels, educational institutions, and professional events.</p>
                <ul>
                    <li>Keynote presentations</li>
                    <li>Panel discussions</li>
                    <li>Educational seminars</li>
                </ul>
            </div>
        </div>
        
        <div class="content-card contact-form-card" data-aos="fade-up" data-aos-delay="300">
            <h3>Contact Information Required</h3>
            <p>When reaching out to schedule a meeting, please include:</p>
            <div class="info-list">
                <div class="info-item">
                    <i class="fas fa-check-circle"></i>
                    <span>Purpose of consultation or engagement</span>
                </div>
                <div class="info-item">
                    <i class="fas fa-check-circle"></i>
                    <span>Preferred dates and times</span>
                </div>
                <div class="info-item">
                    <i class="fas fa-check-circle"></i>
                    <span>Duration needed</span>
                </div>
                <div class="info-item">
                    <i class="fas fa-check-circle"></i>
                    <span>Any specific topics or questions</span>
                </div>
                <div class="info-item">
                    <i class="fas fa-check-circle"></i>
                    <span>Contact information for follow-up</span>
                </div>
            </div>
        </div>
        
        <div class="content-card cta-card" data-aos="fade-up" data-aos-delay="400">
            <h3>Get Started</h3>
            <p>Ready to schedule? Send an email to begin the conversation.</p>
            <a href="mailto:saeed@saeedahmad.com?subject=Meeting Request" class="btn btn-primary btn-large">
                <i class="fas fa-envelope"></i> Email to Schedule
            </a>
        </div>
        """
    },
    "sponsars": {
        "title": "Sponsors & Partners",
        "subtitle": "Supporting Organizations & Collaborations",
        "content": """
        <div class="content-card" data-aos="fade-up">
            <div class="card-icon">
                <i class="fas fa-hands-helping"></i>
            </div>
            <h3>Partnerships & Support</h3>
            <p>Information about sponsors, partners, and supporting organizations will be displayed here.</p>
        </div>
        
        <div class="content-card" data-aos="fade-up" data-aos-delay="100">
            <h3>Collaboration Opportunities</h3>
            <p>Interested in partnering or supporting educational and legal initiatives? Please reach out via the <a href="/contact/">contact page</a> to discuss collaboration opportunities.</p>
        </div>
        
        <div class="content-card cta-card" data-aos="fade-up" data-aos-delay="200">
            <h3>Get Involved</h3>
            <p>For partnership inquiries or sponsorship opportunities, please contact us.</p>
            <a href="/contact/" class="btn btn-primary">
                <i class="fas fa-envelope"></i> Contact for Partnerships
            </a>
        </div>
        """
    }
}

# Enhanced page template with better styling
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Saeed Ahmad</title>
    <meta name="description" content="{title} - Saeed Ahmad, Harvard Law J.D. '24">
    <link rel="stylesheet" href="../styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Source+Serif+Pro:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="nav-content">
                <a href="/" class="logo">Saeed Ahmad</a>
                <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <ul class="nav-menu" id="navMenu">
                    <li><a href="/" class="nav-link">Home</a></li>
                    <li><a href="/education/" class="nav-link">Education</a></li>
                    <li><a href="/skills/" class="nav-link">Skills</a></li>
                    <li><a href="/portfolio/" class="nav-link">Portfolio</a></li>
                    <li><a href="/books/" class="nav-link">Books</a></li>
                    <li><a href="/speaking/" class="nav-link">Speaking</a></li>
                    <li><a href="/press/" class="nav-link">Press</a></li>
                    <li><a href="/contact/" class="nav-link btn-contact">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Page Header -->
    <section class="page-header">
        <div class="container">
            <h1 class="page-title" data-aos="fade-up">{title}</h1>
            <p class="page-subtitle" data-aos="fade-up" data-aos-delay="100">{subtitle}</p>
        </div>
    </section>

    <!-- Main Content -->
    <section class="content-section">
        <div class="container">
            {content}
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-info">
                    <h3>Saeed Ahmad</h3>
                    <p>Harvard Law School J.D. '24</p>
                    <p>Visiting Fellow, Religious Freedom Clinic</p>
                </div>
                <div class="footer-links">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="/education/">Education</a></li>
                        <li><a href="/portfolio/">Portfolio</a></li>
                        <li><a href="/speaking/">Speaking</a></li>
                        <li><a href="/contact/">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h4>Connect</h4>
                    <div class="footer-social">
                        <a href="https://www.linkedin.com/in/saeedahmad-" target="_blank" aria-label="LinkedIn">
                            <i class="fab fa-linkedin"></i>
                        </a>
                        <a href="https://twitter.com/_saeedahmad" target="_blank" aria-label="Twitter">
                            <i class="fab fa-twitter"></i>
                        </a>
                        <a href="https://www.instagram.com/_saeedahmad/" target="_blank" aria-label="Instagram">
                            <i class="fab fa-instagram"></i>
                        </a>
                        <a href="https://www.facebook.com/saeedahmaducla" target="_blank" aria-label="Facebook">
                            <i class="fab fa-facebook"></i>
                        </a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2025 Saeed Ahmad. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="../script.js"></script>
</body>
</html>
"""

# Generate all pages
for page_name, page_data in pages.items():
    html_content = template.format(
        title=page_data['title'],
        subtitle=page_data['subtitle'],
        content=page_data['content']
    )
    
    page_dir = f'/workspaces/saeed-ahmad/site/{page_name}'
    os.makedirs(page_dir, exist_ok=True)
    
    with open(f'{page_dir}/index.html', 'w') as f:
        f.write(html_content)
    
    print(f'✓ Polished {page_name}/index.html')

print('\n✅ All pages polished successfully!')
