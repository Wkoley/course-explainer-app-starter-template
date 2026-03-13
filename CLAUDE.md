# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup
python -m venv venv
source venv/Scripts/activate   # Windows bash
pip install -r requirements.txt

# Run
python src/app.py              # Dev server at http://127.0.0.1:5000

# Test
python -m unittest discover -s tests

# Run a single test
python -m unittest tests.test_app.AppTestCase.test_index
```

## Architecture

Flask MVC starter template for a course listing app.

- **[src/app.py](src/app.py)** — Flask entry point; registers 2 routes (`/` and `/course/<course_id>`)
- **[src/models.py](src/models.py)** — `Course` class + hardcoded list of 3 course instances
- **[src/views.py](src/views.py)** — View functions (`index`, `course`) that render Jinja2 templates
- **[src/templates/](src/templates/)** — `layout.html` (base), `index.html`, `course.html`
- **[tests/test_app.py](tests/test_app.py)** — Adds `src/` to `sys.path` before importing `app`

## Known Issues in Starter Template

- `course()` view passes only `course_id` to `course.html`, but the template expects a full `course` object with a `topics` attribute — requires adding course lookup logic in `views.py`
- `index.html` uses `{% include %}` instead of `{% extends %}` like `course.html` does — template inheritance is inconsistent
- `python-dotenv` is in requirements but no `.env` file is used yet


## Add Unit tests

- Whenever you did any changes add unit tests and run and make sure the tests passes.