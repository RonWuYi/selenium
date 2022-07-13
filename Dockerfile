FROM ubuntu:22.04

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# runtime dependencies
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		build-essential \
		vim \
		neovim \
		curl \
		iproute2 \
	; \

	apt update; \
	apt install -y --no-install-recommends \
		zsh \
	; \

	chsh -s $(which zsh); \

	sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"; \
	rm -rf /var/lib/apt/lists/*
	
CMD ["zsh"]