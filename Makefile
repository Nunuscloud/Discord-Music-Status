# 🎧 Vibe Check - Makefile
# Simplifies running and managing the Discord Music Status script

PYTHON := python
SCRIPT := run_rpc_youtubemusic.py
REQUIREMENTS := requirements.txt
LOGFILE := last-run.log

# 🏃 Run the script
run:
	$(PYTHON) $(SCRIPT)

# 📦 Install dependencies
install:
	$(PYTHON) -m pip install -r $(REQUIREMENTS)

# 🧹 Clean up log files
clean:
	-del /Q $(LOGFILE) 2>nul || true
	rm -f $(LOGFILE) || true

# 🆘 Help command
help:
	@echo "Usage:"
	@echo "  make install   - Install required Python packages"
	@echo "  make run       - Run the Discord music status script"
	@echo "  make clean     - Remove log or temporary files"
	@echo "  make help      - Show this help message"
