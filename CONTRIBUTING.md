

```markdown
# Contributing to Baseball Strategy Assistant

Thank you for your interest in contributing to the Baseball Strategy Assistant! We welcome contributions from everyone, whether you're fixing bugs, improving documentation, or proposing new features. Please take a moment to review this guide to ensure a smooth and enjoyable contribution process.

---

## 🚀 How to Contribute

### 1. **Report Bugs**
If you find a bug, please [open an issue](https://github.com/Eusha425/baseball-strategy-assistant/issues) and include:
- A clear description of the problem.
- Steps to reproduce the issue.
- Screenshots or error messages (if applicable).

### 2. **Suggest Features**
Have an idea to improve the project? Open an issue and:
- Describe the feature or enhancement.
- Explain why it would be valuable.
- Provide examples or mockups (if possible).

### 3. **Submit Pull Requests**
Want to contribute code? Follow these steps:
1. **Fork the repository** and clone it locally.
2. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and test them thoroughly.
4. Commit your changes with a clear and descriptive message:
   ```bash
   git commit -m "Add: New feature to explain pitch types"
   ```
5. Push your branch to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a **Pull Request (PR)** and describe your changes in detail.

---

## 🛠️ Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/baseball-strategy-assistant.git
   cd baseball-strategy-assistant
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app locally**:
   ```bash
   streamlit run main.py
   ```

---

## 🧪 Testing

Before submitting a PR, ensure your changes pass all tests:
1. Run the app and verify functionality.
2. Check for linting errors:
   ```bash
   pylint mlb_client gemini_client main.py
   ```
3. Format your code:
   ```bash
   black .
   ```


---

## 🙌 Thank You!

Your contributions help make this project better for everyone. I appreciate your time and effort!

---

## 📝 License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
