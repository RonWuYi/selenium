FROM i386/ubuntu:18.04

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
		make \
		doxygen \
		zip \ 
		gcc-multilib \
		libssl-dev \
		libssl-dev:i386 \
		gcovr \
		ggcov \
		lcov \
		git \
		wget \
		cmake \
		ca-certificates \
		autoconf \
		automake \
		autotools-dev \
		python3 \
		libmpc-dev \
		libmpfr-dev \
		libgmp-dev \
		gawk \
		build-essential \
		bison \
		flex \
		texinfo \
		gperf \
		libtool \
		patchutils \
		bc \
		zlib1g-dev \
		libexpat-dev \
	; \
	mkdir /opt/toolchains \
	&& chmod -R 775 /opt/toolchains/ \
	&& git clone https://github.com/riscv/riscv-gnu-toolchain \
	&& cd riscv-gnu-toolchain \
	&& ./configure --prefix=/opt/toolchains/riscv32-unknown-elf-gcc --with-arch=rv32im --with-abi=ilp32 \
	&& make \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf riscv-gnu-toolchain/

CMD ["bash"]