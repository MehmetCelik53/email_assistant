# Email Assistant

LangGraph-powered Email Assistant agent that can automatically triage, respond to, and manage emails with human-in-the-loop (HITL) capabilities.

## Features

- **Email Triage**: Automatically classifies emails as "ignore", "notify", or "respond"
- **Human-in-the-Loop**: Provides interrupts for review and editing of AI-generated responses
- **Meeting Scheduling**: Can schedule meetings and check calendar availability
- **Tool Integration**: Supports multiple tools for email and calendar management

## Project Structure

- `app.ipynb` - Main Jupyter notebook with the complete email assistant implementation
- `prompts.py` - Email triage and agent system prompts
- `prompt_templates.py` - Tool descriptions for HITL workflow
- `schemas.py` - Pydantic schemas for state management
- `utils.py` - Utility functions for email parsing and formatting

## Key Components

### Email Triage
The system automatically classifies incoming emails into three categories:
1. **IGNORE** - Emails not worth responding to (newsletters, spam, etc.)
2. **NOTIFY** - Important information that doesn't require a response
3. **RESPOND** - Emails that need a direct response

### Human-in-the-Loop Features
- Review AI-generated email drafts before sending
- Edit meeting requests and scheduling details
- Provide feedback on responses
- Accept, ignore, or modify AI suggestions

### Tools Available
- `write_email` - Draft and send email responses
- `schedule_meeting` - Create calendar meetings
- `check_calendar_availability` - Find available time slots
- `Question` - Ask user for clarification
- `Done` - Mark task completion

## Usage

The system processes emails through a multi-step workflow:

1. **Triage Router** - Analyzes incoming emails and decides routing
2. **Interrupt Handlers** - Provide human oversight at key decision points
3. **Response Agent** - Generates appropriate responses using available tools

Run the `app.ipynb` notebook to see the email assistant in action with various scenarios.

## Configuration

The system includes configurable preferences for:
- Background information (user context)
- Triage instructions (classification rules)
- Response preferences (tone, style, requirements)
- Calendar preferences (meeting durations, scheduling)

## Dependencies

- LangGraph for workflow orchestration
- LangChain for LLM integration
- Pydantic for data validation
- OpenAI for language model capabilities

## Development

This project demonstrates advanced LangGraph patterns including:
- Multi-agent workflows
- Human-in-the-loop interrupts
- State management with checkpointing
- Tool calling with validation
- Dynamic routing based on content analysis

Built with Python 3.13+ and modern AI/ML libraries for production-ready email automation.

---

## 🇹🇷 Türkçe Özet

Email Assistant, LangGraph ve LangChain teknolojileri ile geliştirilmiş, e-posta yönetimini otomatikleştiren gelişmiş bir AI asistan sistemidir. İnsan onayı gerektiren süreçlerle (Human-in-the-Loop) güvenli ve kontrollü e-posta işlemleri sunar.

### 🎯 Ana Özellikler

**Akıllı E-posta Sınıflandırması**
- **IGNORE (Yoksay)**: Haber bültenleri, spam, önemsiz e-postalar
- **NOTIFY (Bilgilendir)**: Önemli ama yanıt gerektirmeyen bilgiler
- **RESPOND (Yanıtla)**: Direkt yanıt gerektiren e-postalar
- **Otomatik Triage**: AI ile akıllı sınıflandırma

**İnsan-Döngü-İçi (HITL) Kontrol**
- **Taslak İnceleme**: AI'ın hazırladığı yanıtları önce göster
- **Düzenleme İmkanı**: Cevapları gönderilmeden önce değiştir
- **Onay Mekanizması**: Her kritik işlem için kullanıcı onayı
- **Geri Bildirim**: AI'ın öğrenmesi için feedback verme

**Takvim ve Toplantı Yönetimi**
- **Otomatik Randevu**: Uygun saatleri bulup toplantı oluştur
- **Müsaitlik Kontrolü**: Takvim entegrasyonu ile çakışma önleme
- **Akıllı Zamanlama**: Tercihler ve kurallar dahilinde planlama
- **Toplantı Detayları**: Lokasyon, katılımcı, ajanda yönetimi

### 🛠️ Teknik Mimari

**LangGraph İş Akışı**
- **Çoklu Ajan Sistemi**: Uzmanlaşmış ajanlar ve koordinasyon
- **Durum Yönetimi**: Checkpointing ile süreç takibi
- **Dinamik Yönlendirme**: İçerik analizine göre karar alma
- **Araç Entegrasyonu**: Çeşitli servislerin seamless kullanımı

**Kullanılan Teknolojiler**
- **LangGraph**: İş akışı orkestrayonu
- **LangChain**: LLM entegrasyonu ve zincirlemesi
- **Pydantic**: Data validation ve type safety
- **OpenAI GPT**: Doğal dil işleme yetenekleri

### 💡 Kullanım Senaryoları

**İş Hayatı**
- **Müşteri E-postaları**: Otomatik sınıflandırma ve yanıtlama
- **Toplantı Koordinasyonu**: Randevu oluşturma ve yönetimi
- **E-posta Backlog**: Birikmiş e-postaları hızlı işleme
- **Priorite Yönetimi**: Önemli e-postaları öne çıkarma

**Kişisel Kullanım**
- **E-posta Temizliği**: Spam ve gereksiz e-postaları filtreleme
- **Otomatik Yanıtlar**: Rutin sorulara hızlı cevap
- **Takvim Planlaması**: Sosyal ve iş randevularını organize etme
- **Zaman Yönetimi**: E-posta işlerinde verimlilik artışı

### 🚀 Nasıl Çalışır?

1. **E-posta Gelişi**: Sistem yeni e-postaları otomatik analiz eder
2. **Akıllı Sınıflandırma**: Triage router ile kategorizasyon
3. **Yanıt Üretimi**: Uygun durumlarda AI yanıt taslağı hazırlar
4. **İnsan Onayı**: Kritik noktalarda kullanıcı müdahalesi
5. **İşlem Tamamlama**: Onaylanan işlemler otomatik gerçekleşir

### 🎓 Öğrenme Değeri

Bu proje şunları öğretir:
- **LangGraph Patterns**: Gelişmiş iş akışı tasarımları
- **HITL Implementation**: İnsan kontrolü entegrasyonu
- **State Management**: Karmaşık durum yönetimi
- **Tool Orchestration**: Çoklu araç koordinasyonu
- **Production Patterns**: Gerçek dünya AI uygulamaları

### 📦 Proje Dosyaları

- **`app.ipynb`**: Ana uygulama ve demo senaryoları
- **`prompts.py`**: AI sistem komutları ve triage kuralları
- **`schemas.py`**: Veri yapıları ve validasyon kuralları
- **`utils.py`**: Yardımcı fonksiyonlar ve formatlamalar

Bu sistem, e-posta yönetiminde AI'ın gücünü güvenli ve kontrollü şekilde kullanarak günlük iş yükünüzü önemli ölçüde azaltır.