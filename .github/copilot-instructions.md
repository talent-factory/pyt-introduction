# Copilot-Anweisungen für pyt-introduction

Dieses Dokument enthält wichtige Informationen für KI-Coding-Assistenten zur effektiven Arbeit mit diesem Repository.

## 🎯 Projektübersicht

- **Ziel**: Deutschsprachiger Python-Einführungskurs für absolute Programmieranfänger
- **Zielgruppe**: Anfänger ohne Vorkenntnisse
- **Sprache**: Alle Inhalte auf Deutsch (Code-Kommentare, Dokumentation, Variablennamen)

## 🏗️ Architektur & Komponenten

### Kursstruktur
- Didaktische Progression über 5 Kursabende
- Jupyter Notebooks als Hauptlernmaterial
- Übungsaufgaben mit steigendem Schwierigkeitsgrad
- Mini-Projekte als Praxisanwendung

### Verzeichnisstruktur
```
pyt-introduction/
├── ipynb/                # Jupyter Notebooks (Hauptlernmaterial)
├── exercise/             # Übungsaufgaben
├── solutions/            # Musterlösungen
├── docs/                 # Dokumentation
├── introcs/             # CS-Beispielmodule
└── stdlib/              # Hilfsmodule für Einsteiger
```

## 💻 Entwicklungs-Workflows

### Package Management
```bash
uv sync                      # Abhängigkeiten installieren
uv run python <skript>       # Python-Skript ausführen
```

### Test-Workflow
- Doctests für einfache Funktionsvalidierung
- Test-Ausführung: `python -m doctest <datei.py>`
- Testfälle in Docstrings integrieren

### Code-Qualität
- Black für Formatierung (max. 100 Zeichen/Zeile)
- PEP 8 Konventionen befolgen
- Deutsche Docstrings und Kommentare

## 📝 Coding Konventionen

### Stilrichtlinien
- Einrückung: 4 Leerzeichen
- Klassen: `PascalCase`
- Funktionen/Variablen: `snake_case`
- Konstanten: `UPPER_CASE`

### Docstring-Format
```python
def funktion_name(parameter: str) -> int:
    """
    Kurze Beschreibung der Funktion.
    
    Args:
        parameter: Beschreibung des Parameters
        
    Returns:
        Beschreibung des Rückgabewerts
        
    Examples:
        >>> funktion_name("test")
        42
    """
    return 42
```

## 🔗 Integrationspunkte

### stdlib-Module
- Custom I/O-Funktionen (`stdio`, `stddraw`)
- Nur für Lehrzwecke, nicht für Production-Code
- Beispielimport: `from stdlib import stdio`

### introcs-Module
- Klassische CS-Beispiele (Algorithmen, Datenstrukturen)
- Abhängig von stdlib-Modulen
- Fokus auf Lernbarkeit statt Effizienz

## ⚠️ Wichtige Hinweise

1. Alle Nutzer-sichtbaren Texte auf Deutsch
2. Fehlerbehandlung für Anfänger verständlich gestalten
3. Code-Beispiele didaktisch aufbereiten
4. Bei Änderungen Doctest-Beispiele aktualisieren
5. Branches `main` und `develop` sind geschützt