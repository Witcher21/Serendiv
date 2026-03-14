<template>
  <q-page class="bg-[#030303] text-white relative w-full font-serif selection:bg-teal-700 selection:text-white">
    
    <!-- Audio Elements -->
    <audio ref="audioPlayer" loop preload="auto">
      <source :src="currentVibe.audio" type="audio/mpeg" />
    </audio>
    <audio ref="clickSound" src="https://assets.mixkit.co/active_storage/sfx/2568/2568-preview.mp3" preload="auto"></audio>

    <!-- NAVIGATION -->
    <nav class="fixed top-0 left-0 w-full z-50 px-6 py-6 md:px-16 flex justify-between items-center transition-all duration-700 font-sans" :class="{'bg-[#050505]/90 backdrop-blur-2xl border-b border-white/5 py-4 shadow-2xl': scrolled > 50}">
      <div class="text-2xl md:text-3xl font-black tracking-[0.3em] uppercase text-white cursor-pointer select-none" @click="scrollTo('#hero')">
        Seren<span class="text-teal-500 font-light">div</span>.
      </div>
      
      <!-- Desktop Menu -->
      <div class="hidden lg:flex items-center gap-12 font-medium tracking-[0.2em] text-[11px] uppercase">
        <a @click.prevent="scrollTo('#about')" class="cursor-pointer text-gray-400 hover:text-white transition-colors relative group">
          The Story
          <span class="absolute -bottom-2 left-0 w-0 h-[1px] bg-teal-400 transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a @click.prevent="scrollTo('#destinations')" class="cursor-pointer text-gray-400 hover:text-white transition-colors relative group">
          Destinations
          <span class="absolute -bottom-2 left-0 w-0 h-[1px] bg-teal-400 transition-all duration-300 group-hover:w-full"></span>
        </a>
        <a @click.prevent="scrollTo('#concierge')" class="cursor-pointer text-gray-400 hover:text-white transition-colors relative group">
          Services
          <span class="absolute -bottom-2 left-0 w-0 h-[1px] bg-teal-400 transition-all duration-300 group-hover:w-full"></span>
        </a>
        
        <div class="w-[1px] h-6 bg-white/20 mx-2"></div>
        
        <button @click="toggleAudio" class="group flex items-center justify-center gap-3 hover:text-teal-400 transition-all">
          <div class="w-8 h-8 rounded-full border border-white/20 flex items-center justify-center group-hover:border-teal-400/50 transition-colors">
            <q-icon :name="isAudioPlaying ? 'volume_up' : 'volume_off'" size="xs" :class="isAudioPlaying ? 'text-teal-400' : 'text-gray-400'" />
          </div>
          <span class="text-[10px] text-gray-400 group-hover:text-white hidden xl:block">{{ isAudioPlaying ? 'SOUND ON' : 'SOUND OFF' }}</span>
        </button>
        
        <button @click="contactModal = true; playClick()" class="px-8 py-3 bg-white text-black hover:bg-teal-500 hover:text-white rounded-none transition-all duration-500 font-bold uppercase tracking-[0.2em] text-[10px] relative overflow-hidden group">
          <span class="relative z-10">Bespoke Inquiry</span>
          <div class="absolute inset-0 bg-teal-600 transform scale-x-0 origin-left group-hover:scale-x-100 transition-transform duration-500 ease-out z-0"></div>
        </button>
      </div>

      <!-- Mobile Menu Toggle -->
      <button class="lg:hidden w-12 h-12 flex items-center justify-center text-white" @click="mobileMenu = !mobileMenu; playClick()">
        <q-icon :name="mobileMenu ? 'close' : 'menu'" size="sm" />
      </button>
    </nav>

    <!-- Mobile Screen -->
    <div class="fixed inset-0 z-40 bg-[#050505] flex flex-col items-center justify-center gap-10 lg:hidden transition-transform duration-700 ease-[cubic-bezier(0.76,0,0.24,1)] font-sans uppercase tracking-[0.3em]" :class="mobileMenu ? 'translate-y-0' : '-translate-y-full'">
      <a @click.prevent="scrollTo('#about'); mobileMenu = false" class="text-3xl font-light hover:text-teal-400">The Story</a>
      <a @click.prevent="scrollTo('#destinations'); mobileMenu = false" class="text-3xl font-light hover:text-teal-400">Destinations</a>
      <a @click.prevent="scrollTo('#concierge'); mobileMenu = false" class="text-3xl font-light hover:text-teal-400">Services</a>
      <button @click="toggleAudio" class="text-sm text-gray-400 mt-10 border border-white/20 px-6 py-2 rounded-full">
        {{ isAudioPlaying ? 'Mute Atmosphere' : 'Play Atmosphere' }}
      </button>
      <button @click="contactModal = true; mobileMenu = false" class="mt-8 px-12 py-4 bg-teal-600 text-white text-sm font-bold">INQUIRE NOW</button>
    </div>

    <!-- 1. HERO / AURA DISCOVERY -->
    <section id="hero" class="relative w-full h-screen flex flex-col justify-center px-6 md:px-16 overflow-hidden bg-black">
      
      <!-- Stable High-Res Image Backgrounds -->
      <div class="absolute inset-0 z-0">
        <div class="absolute inset-0 bg-gradient-to-t from-[#030303] via-[#030303]/60 to-black/50 z-10"></div>
        
        <!-- Ancient Image: Sigiriya / High-end Heritage -->
        <img 
          src="https://images.unsplash.com/photo-1734279135115-6d8984e08206?q=80&w=2500&auto=format&fit=crop&ixlib=rb-4.1.0" 
          class="w-full h-full object-cover absolute inset-0 transition-opacity duration-[2s] ease-in-out transform scale-100 filter brightness-90 contrast-[1.1]" 
          :class="currentVibe.id === 'ancient' ? 'opacity-100' : 'opacity-0 scale-105'"
        />
        
        <!-- Wild Image: Leopard / Safari -->
        <img 
          src="https://images.unsplash.com/photo-1617867644194-550af3ae2c56?q=80&w=2500&auto=format&fit=crop&ixlib=rb-4.1.0" 
          class="w-full h-full object-cover absolute inset-0 transition-opacity duration-[2s] ease-in-out transform scale-100 filter brightness-[0.85] contrast-[1.15]" 
          :class="currentVibe.id === 'wild' ? 'opacity-100' : 'opacity-0 scale-105'"
        />
        
        <!-- Serene Image: Tropical High-end Beach / Mirissa -->
        <img 
          src="https://images.unsplash.com/photo-1561150018-8bb356679537?q=80&w=2500&auto=format&fit=crop&ixlib=rb-4.1.0" 
          class="w-full h-full object-cover absolute inset-0 transition-opacity duration-[2s] ease-in-out transform scale-100 filter brightness-[0.8] contrast-[1.2]" 
          :class="currentVibe.id === 'serene' ? 'opacity-100' : 'opacity-0 scale-105'"
        />
      </div>

      <!-- WebGL Layer for Particle Dust -->
      <div ref="heroCanvas" class="absolute inset-0 z-[5] pointer-events-none opacity-40 mix-blend-screen"></div>

      <!-- Content Grid -->
      <div class="relative z-20 w-full max-w-[1700px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-12 items-center mt-20">
        
        <!-- Left Title -->
        <div class="lg:col-span-8 flex flex-col relative z-20">
          <div class="overflow-hidden mb-6 md:mb-10">
            <p class="hero-subtitle text-teal-400 font-sans uppercase tracking-[0.5em] text-[10px] md:text-xs font-bold flex items-center gap-6 opacity-0">
              <span class="w-16 h-[1px] bg-teal-500 hidden md:inline-block"></span>
              The Absolute Sri Lankan Journey
            </p>
          </div>
          <h1 class="hero-title text-[3.5rem] sm:text-[4.5rem] md:text-[5.5rem] lg:text-[6.5rem] font-medium leading-[1] tracking-tighter drop-shadow-2xl text-white">
            <div class="overflow-hidden pb-2"><span class="block translate-y-full">A journey</span></div>
            <div class="overflow-hidden pb-4"><span class="block translate-y-full italic font-light text-white/90 pr-12">beyond.</span></div>
          </h1>
          <div class="mt-8 md:mt-12 relative overflow-hidden hero-desc opacity-0 w-full max-w-lg lg:max-w-[85%]">
            <div class="absolute left-0 top-0 bottom-0 w-[2px] bg-gradient-to-b from-teal-500 via-teal-500/20 to-transparent"></div>
            <div class="pl-6 md:pl-10">
              <div class="min-h-[90px] md:min-h-[110px]">
                <transition name="vibe-text" mode="out-in">
                  <p :key="currentVibe.id" class="text-white/80 font-sans font-light tracking-wide text-sm md:text-base leading-[1.8] text-shadow-md pr-4">
                    {{ currentVibe.description }}
                  </p>
                </transition>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Selectors -->
        <div class="lg:col-span-4 flex flex-col items-start lg:items-end w-full lg:mt-24 font-sans">
          <div class="w-full max-w-[360px] relative z-10">
            
            <div class="text-[9px] uppercase tracking-[0.4em] text-white/60 mb-10 flex items-center gap-6">
              <span class="font-bold">Atmosphere</span>
              <div class="flex-1 h-[1px] bg-white/20"></div>
              <span class="text-teal-400 font-bold">0{{ activeVibeIndex + 1 }} / 03</span>
            </div>
            
            <div class="space-y-2 relative border-l border-white/10 pl-10">
              <div class="absolute left-[-1px] w-[3px] h-[64px] bg-teal-500 transition-all duration-700 ease-[cubic-bezier(0.76,0,0.24,1)] shadow-[0_0_15px_rgba(20,184,166,0.6)]" :style="`top: ${activeVibeIndex * (64 + 8)}px`"></div>

              <button 
                v-for="(vibe, index) in vibes" :key="vibe.id"
                @click="setVibe(vibe, index)"
                class="w-full h-16 flex items-center justify-between group/btn transition-all duration-300 relative"
              >
                <span class="text-2xl md:text-3xl font-light tracking-widest uppercase transition-colors duration-500 drop-shadow-md" :class="currentVibe.id === vibe.id ? 'text-white font-medium' : 'text-white/30 group-hover/btn:text-white/70'">
                  {{ vibe.name }}
                </span>
                <span class="text-[9px] tracking-[0.4em] font-bold opacity-0 group-hover/btn:opacity-100 transition-opacity" :class="{'opacity-100 text-teal-400': currentVibe.id === vibe.id}">
                  ACTIVATE
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Scroll Indicator -->
      <div class="absolute bottom-10 left-6 md:left-16 z-20 flex items-center gap-4 cursor-pointer group" @click="scrollTo('#about')">
        <div class="w-10 h-10 rounded-full border border-white/30 flex items-center justify-center group-hover:border-teal-500 transition-colors duration-500 bg-black/20 backdrop-blur-sm">
          <q-icon name="arrow_downward" size="xs" class="text-white group-hover:text-teal-400 group-hover:translate-y-1 transition-all duration-500" />
        </div>
        <span class="font-sans text-[9px] uppercase tracking-[0.3em] text-white/70 group-hover:text-white transition-colors">Discover Quality</span>
      </div>
    </section>

    <!-- PREMIUM CINEMATIC SEPARATOR 0 (Hero -> About) -->
    <section class="min-h-[40vh] md:min-h-[50vh] w-full bg-[#050505] relative flex flex-col justify-center items-center z-20 border-t border-white/[0.05]">
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-teal-900/5 via-[#050505] to-[#030303]"></div>
      
      <div class="gs-reveal flex flex-col items-center relative z-10 w-full px-6">
        <h3 class="text-2xl md:text-4xl lg:text-[3.5rem] font-serif font-light text-center text-white/90 leading-[1.2] tracking-wide drop-shadow-2xl">
          An unspoken elegance.<br/>
          <span class="italic text-teal-400 font-medium mt-4 block">A timeless sanctuary.</span>
        </h3>
        <div class="w-[1px] h-16 md:h-24 bg-gradient-to-t from-transparent via-white/20 to-white mt-8 md:mt-12"></div>
      </div>
    </section>

    <!-- 2. THE STORY / BRAND -->
    <section id="about" class="py-32 md:py-48 px-6 md:px-16 bg-[#030303] relative border-t border-white/5">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-teal-900/10 via-[#030303] to-[#030303] pointer-events-none"></div>

      <div class="max-w-[1700px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-16 md:gap-24 items-center">
        <!-- Visual -->
        <div class="lg:col-span-5 relative w-full aspect-square md:aspect-[3/4] group gs-reveal">
          <div class="absolute inset-0 bg-teal-900/40 translate-x-4 translate-y-4 -z-10 transition-transform duration-700 ease-out"></div>
          <img src="https://images.pexels.com/photos/3389817/pexels-photo-3389817.jpeg?auto=compress&cs=tinysrgb&w=1200" alt="Sri Lanka Heritage" class="w-full h-full object-cover filter brightness-90 contrast-125 transition-all duration-[2s]" />
          <!-- Floating badge -->
          <div class="absolute -right-8 top-1/2 -translate-y-1/2 bg-[#050505] p-6 border border-white/10 flex flex-col items-center gap-2 hidden md:flex font-sans shadow-2xl hover:scale-105 transition-transform duration-300">
            <q-icon name="explore" size="md" class="text-teal-500 animate-pulse" />
            <span class="text-[9px] uppercase tracking-[0.2em] mt-2 text-white/80">Established</span>
            <span class="text-lg font-bold text-white">2026</span>
          </div>
        </div>

        <!-- Copy -->
        <div class="lg:col-span-7 gs-reveal">
          <div class="flex items-center gap-6 mb-12 font-sans">
            <div class="w-12 h-[1px] bg-teal-500"></div>
            <span class="uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold">The Serendiv Ethos</span>
          </div>
          <h2 class="text-5xl md:text-7xl font-medium leading-[1.1] mb-12 text-white drop-shadow-2xl">
            Discover the <br/>
            <span class="italic text-teal-300 font-light">Pearl of the Indian Ocean.</span>
          </h2>
          <div class="max-w-xl font-sans font-light leading-relaxed text-base md:text-lg space-y-8">
            <p class="text-white/75 leading-[1.9]">
              Sri Lanka, historically known as Serendib and Ceylon, is a tear-drop shaped island boasting a rich legacy of over 2,500 years. It is a land where serendipity is not just a word, but a way of life—a place where every journey unfolds unexpected beauty.
            </p>
            <p class="text-white/75 leading-[1.9]">
              We design tailor-made journeys that showcase the island's supreme diversity. From the ancient, fresco-adorned rock fortress of Sigiriya (an 8th Wonder of the World) to the misty, emerald tea estates of Nuwara Eliya, and the leopard-dense jungles of Yala—we elevate your island expedition to a masterpiece.
            </p>
          </div>
          
          <div class="mt-20 flex flex-col md:flex-row gap-12 md:gap-20 border-t border-white/10 pt-12 font-sans w-full">
            <div class="flex-1">
              <div class="text-3xl md:text-4xl font-light text-white mb-3">Private</div>
              <div class="text-[9px] uppercase tracking-[0.3em] text-teal-500 font-bold">Aviation & Jets</div>
            </div>
            <div class="hidden md:block w-[1px] bg-white/10"></div>
            <div class="flex-1">
              <div class="text-3xl md:text-4xl font-light text-white mb-3">500+</div>
              <div class="text-[9px] uppercase tracking-[0.3em] text-teal-500 font-bold">Exclusive Estates</div>
            </div>
            <div class="hidden md:block w-[1px] bg-white/10"></div>
            <div class="flex-1 w-full md:w-auto mt-8 md:mt-0 pt-8 md:pt-0 border-t border-white/10 md:border-none">
              <div class="text-3xl md:text-4xl font-light text-white mb-3">24/7</div>
              <div class="text-[9px] uppercase tracking-[0.3em] text-teal-500 font-bold">Concierge Service</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- PREMIUM CINEMATIC SEPARATOR 1 -->
    <section class="min-h-[50vh] md:min-h-[70vh] w-full bg-[#040404] relative flex flex-col justify-center items-center z-20 border-t border-white/[0.05]">
      <!-- Deep subtle radial glow -->
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-teal-900/10 via-[#040404] to-[#030303]"></div>
      
      <div class="gs-reveal flex flex-col items-center relative z-10 w-full px-6">
        <div class="w-[1px] h-24 md:h-40 bg-gradient-to-b from-transparent via-teal-500/50 to-teal-500 mb-10 md:mb-16"></div>
        
        <h3 class="text-3xl md:text-5xl lg:text-[4.5rem] font-serif font-light text-center text-white/90 leading-[1.2] tracking-wide drop-shadow-2xl">
          Beyond the map.<br/>
          <span class="italic text-teal-400 font-medium mt-4 block">Into the sublime.</span>
        </h3>
        
        <div class="w-[1px] h-24 md:h-40 bg-gradient-to-t from-transparent via-white/20 to-white mt-10 md:mb-0"></div>
      </div>
    </section>

    <!-- INTERACTIVE SRI LANKA MAP SECTION -->
    <section class="py-32 md:py-48 px-6 md:px-16 bg-[#030303] border-t border-white/5 relative overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-teal-900/15 via-[#030303] to-[#030303] pointer-events-none"></div>

      <div class="max-w-[1700px] mx-auto relative z-10">
        <!-- Section Header -->
        <div class="gs-reveal flex flex-col md:flex-row md:items-end justify-between mb-20 md:mb-32">
          <div>
            <span class="uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold flex items-center gap-4 mb-6 font-sans">
              <span class="w-8 h-[1px] bg-teal-500"></span>
              Discover the Island
            </span>
            <h2 class="text-5xl md:text-[6rem] font-serif font-medium leading-none tracking-tighter text-white drop-shadow-md">
              Explore<br/>
              <span class="italic font-light text-teal-300">Sri Lanka.</span>
            </h2>
          </div>
          <p class="mt-8 md:mt-0 max-w-sm text-white/60 font-sans font-light text-sm md:text-base leading-relaxed md:border-l border-white/10 md:pl-6">
            Click on any location to experience a cinematic preview of what awaits you in that corner of the island.
          </p>
        </div>

        <!-- Map + Info Grid -->
        <div class="gs-reveal grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">

          <!-- SVG Map -->
          <!-- Mapbox Map Container -->
          <div class="relative flex items-center justify-center w-full h-[350px] md:h-[450px] lg:h-[600px] rounded-3xl overflow-hidden border border-white/10 shadow-[0_0_60px_rgba(20,184,166,0.1)] group">
            <div id="mapbox-container" class="absolute inset-0 w-full h-full bg-black"></div>
            <!-- Ambient glow behind map -->
            <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-teal-900/10 via-transparent to-transparent pointer-events-none z-10"></div>
          </div>

          <!-- Right Side Info Panel -->
          <div class="flex flex-col gap-6 font-sans">
            <transition name="vibe-text" mode="out-in">
              <div :key="activeMapLocation?.name || 'default'" class="bg-white/[0.02] border border-white/5 rounded-3xl p-10 md:p-14 relative overflow-hidden min-h-[400px] flex flex-col justify-center">
                <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-teal-900/10 via-transparent to-transparent pointer-events-none"></div>

                <template v-if="activeMapLocation">
                  <div class="relative z-10">
                    <span class="text-[9px] uppercase tracking-[0.4em] text-teal-400 font-bold block mb-4">{{ activeMapLocation.tag }}</span>
                    <h3 class="text-4xl md:text-5xl font-serif font-light text-white mb-6 leading-tight">{{ activeMapLocation.name }}</h3>
                    <p class="text-white/60 font-light text-sm md:text-base leading-relaxed mb-10 max-w-md">{{ activeMapLocation.desc }}</p>

                    <!-- Video Preview -->
                    <div v-if="activeMapLocation.video" class="relative rounded-2xl overflow-hidden border border-white/10 aspect-video mb-8 group cursor-pointer" @click="playMapVideo(activeMapLocation)">
                      <video ref="mapVideoPreview" :src="activeMapLocation.video" muted loop autoplay playsinline class="w-full h-full object-cover filter brightness-75 group-hover:brightness-100 transition-all duration-700"></video>
                      <div class="absolute inset-0 bg-black/30 group-hover:bg-transparent transition-all duration-500 flex items-center justify-center">
                        <div class="w-16 h-16 rounded-full border-2 border-white/50 flex items-center justify-center group-hover:border-teal-500 group-hover:scale-110 transition-all duration-500 backdrop-blur-sm bg-black/20">
                          <q-icon name="play_arrow" size="md" class="text-white ml-1" />
                        </div>
                      </div>
                    </div>

                    <button @click="contactModal = true; playClick()" class="group flex items-center gap-4 text-[11px] uppercase tracking-[0.4em] font-bold text-white hover:text-teal-400 transition-colors">
                      <span>Explore {{ activeMapLocation.name }}</span>
                      <div class="w-6 h-[1px] bg-white/40 group-hover:w-12 group-hover:bg-teal-500 transition-all duration-500"></div>
                    </button>
                  </div>
                </template>
                <template v-else>
                  <div class="relative z-10 text-center py-12">
                    <div class="w-16 h-16 rounded-full border border-teal-500/30 flex items-center justify-center mx-auto mb-8">
                      <q-icon name="touch_app" size="md" class="text-teal-500 animate-pulse" />
                    </div>
                    <h3 class="text-3xl font-serif font-light text-white/90 mb-4">Select a Location</h3>
                    <p class="text-white/40 font-light text-sm max-w-xs mx-auto">Click any pin on the map to explore a curated destination and watch a cinematic preview.</p>
                  </div>
                </template>
              </div>
            </transition>
          </div>

        </div>
      </div>
    </section>

    <!-- 3. CURATED DESTINATIONS (Luxury Gallery) -->
    <section id="destinations" class="py-32 bg-[#050505] relative overflow-hidden px-6 md:px-16 border-t border-white/5">
      <div class="max-w-[1700px] mx-auto flex flex-col md:flex-row md:items-end justify-between mb-24 md:mb-32 font-sans gs-reveal">
        <div>
          <span class="uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold flex items-center gap-4 mb-6">
            <span class="w-8 h-[1px] bg-teal-500"></span>
            Portfolio
          </span>
          <h2 class="text-5xl md:text-[6.5rem] font-serif font-medium leading-none tracking-tighter drop-shadow-md">Distinctive<br class="hidden md:block" />Locales.</h2>
        </div>
        <div class="mt-8 md:mt-0 max-w-sm text-gray-400 font-light text-sm md:text-base leading-relaxed md:border-l border-white/10 md:pl-6">
          Explore our highly guarded selection of Sri Lanka's most profound environments, curated for uncompromising luxury and deep connection.
        </div>
      </div>

      <transition-group 
        name="dest-list" 
        tag="div" 
        class="max-w-[1700px] mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-10 cursor-crosshair"
      >
        <div v-for="dest in filteredDestinations" :key="dest.id" class="dest-item relative aspect-square md:aspect-[4/5] overflow-hidden group shadow-2xl bg-black rounded-lg" @click="openModal(dest); playClick()">
          <img :src="dest.img" class="absolute inset-0 w-full h-full object-cover filter brightness-[0.6] group-hover:brightness-100 transform scale-105 group-hover:scale-100 transition-all duration-700 ease-out" />
          
          <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent opacity-90 group-hover:opacity-70 transition-opacity duration-700"></div>
          
          <!-- Category Tag -->
          <div class="absolute top-8 left-8 flex items-center gap-3 overflow-hidden font-sans">
            <div class="w-1.5 h-1.5 rounded-full bg-teal-500 relative">
              <div class="absolute inset-0 bg-teal-400 rounded-full animate-ping opacity-50"></div>
            </div>
            <span class="text-[9px] uppercase tracking-[0.3em] font-bold text-white drop-shadow-md transform -translate-y-0 text-shadow-md">{{ dest.tag }}</span>
          </div>

          <!-- Bottom Text Container -->
          <div class="absolute bottom-8 left-8 right-8 text-left transition-transform duration-500 ease-out transform group-hover:-translate-y-4">
            <h3 class="text-3xl md:text-4xl font-serif font-light mb-4 drop-shadow-lg text-white">{{ dest.title }}</h3>
            <!-- Description hidden by default, sliding up on hover -->
            <div class="h-0 overflow-hidden group-hover:h-auto opacity-0 group-hover:opacity-100 transition-all duration-700 font-sans">
              <p class="text-[13px] text-white tracking-wide font-light leading-relaxed mb-6 border-l border-teal-500/50 pl-4 bg-black/30 p-2 backdrop-blur-sm rounded-r-md">
                {{ dest.overview }}
              </p>
              <button class="text-[10px] uppercase tracking-[0.3em] font-bold flex items-center gap-3 text-teal-400 hover:text-white transition-colors drop-shadow-md bg-black/50 px-4 py-2 rounded-full border border-white/10">
                View Itinerary
                <div class="w-6 h-[1px] bg-teal-400 transition-transform duration-300"></div>
              </button>
            </div>
          </div>
        </div>
      </transition-group>
    </section>

    <!-- PREMIUM CINEMATIC SEPARATOR 2 (Destinations -> Concierge) -->
    <section class="min-h-[50vh] md:min-h-[70vh] w-full bg-[#030303] relative flex flex-col justify-center items-center z-20 shadow-[0_0_100px_rgba(0,0,0,0.8)] border-t border-white/[0.05]">
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-teal-900/10 via-[#030303] to-[#050505]"></div>
      
      <div class="gs-reveal flex flex-col items-center relative z-10 w-full px-6">
        <div class="w-[1px] h-24 md:h-40 bg-gradient-to-b from-transparent via-teal-500/50 to-teal-500 mb-10 md:mb-16"></div>
        
        <h3 class="text-3xl md:text-5xl lg:text-[4.5rem] font-serif font-light text-center text-white/90 leading-[1.2] tracking-wide drop-shadow-2xl">
          Where desire meets reality.<br/>
          <span class="italic text-teal-400 font-medium mt-4 block">Frictionless living.</span>
        </h3>
        
        <div class="w-[1px] h-24 md:h-40 bg-gradient-to-t from-transparent via-white/20 to-white mt-10 md:mb-0"></div>
      </div>
    </section>

    <!-- 4. WHITE GLOVE SERVICES -->
    <section id="concierge" class="py-32 px-6 md:px-16 border-t border-white/5 relative overflow-hidden bg-black">
      
      <!-- Section Video Background -->
      <video autoplay loop muted playsinline class="absolute inset-0 w-full h-full object-cover opacity-40 filter grayscale-[50%] contrast-[1.2] pointer-events-none z-0">
        <source src="https://www.shutterstock.com/shutterstock/videos/3800595019/preview/stock-footage-a-powerful-portrait-of-an-asian-male-elephant-roaming-freely-in-miyamina-park-sri-lanka.mp4" type="video/mp4" />
      </video>
      <div class="absolute inset-0 bg-[#030303]/80 pointer-events-none z-10"></div>

      <div class="max-w-[1700px] mx-auto gs-reveal relative z-20">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
          
          <!-- Left Content -->
          <div class="font-sans order-2 lg:order-1">
            <span class="uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold block mb-8">Uncompromising Luxury</span>
            <h2 class="text-5xl md:text-7xl font-serif font-medium mb-8 leading-[1.1]">White Glove<br/>Access.</h2>
            <p class="text-gray-300 font-light text-base md:text-lg mb-12 max-w-md leading-relaxed">
              True luxury is the absence of friction. We handle every detail of your journey, granting you access to Sri Lanka's most guarded secrets and private estates.
            </p>
            
            <div class="space-y-12 border-t border-white/10 pt-12 font-sans overflow-hidden">
              
              <div class="flex items-start gap-8 group">
                 <div class="text-[10px] font-bold text-teal-500 tracking-[0.2em] mt-1 shrink-0 w-8 border-t border-teal-500/50 pt-2">01.</div>
                 <div>
                    <h4 class="text-2xl font-serif font-light text-white mb-3">Chauffeur-Driven Luxury</h4>
                    <p class="text-sm text-gray-400 font-light leading-relaxed max-w-sm">Travel the island in supreme comfort. Our fleet of luxury SUVs is driven by certified, highly experienced Sri Lankan chauffeur-guides fluent in multiple languages.</p>
                 </div>
              </div>

              <div class="flex items-start gap-8 group">
                 <div class="text-[10px] font-bold text-teal-500 tracking-[0.2em] mt-1 shrink-0 w-8 border-t border-teal-500/50 pt-2">02.</div>
                 <div>
                    <h4 class="text-2xl font-serif font-light text-white mb-3">Cultural & Wildlife Experts</h4>
                    <p class="text-sm text-gray-400 font-light leading-relaxed max-w-sm">Gain profound insights. Your journey is accompanied by specialized local experts—from marine biologists in Mirissa to archaeological guides in Polonnaruwa.</p>
                 </div>
              </div>

              <div class="flex items-start gap-8 group">
                 <div class="text-[10px] font-bold text-teal-500 tracking-[0.2em] mt-1 shrink-0 w-8 border-t border-teal-500/50 pt-2">03.</div>
                 <div>
                    <h4 class="text-2xl font-serif font-light text-white mb-3">Tailor-Made Itineraries</h4>
                    <p class="text-sm text-gray-400 font-light leading-relaxed max-w-sm">No two holidays are the same. Our travel designers craft 100% personalized itineraries matching your exact pace, preferences, and dietary requirements.</p>
                 </div>
              </div>

            </div>
          </div>

          <!-- Right Image Gallery -->
          <div class="order-1 lg:order-2 grid grid-cols-2 gap-4 h-[350px] sm:h-[450px] lg:h-[600px] gs-reveal relative">
            <div class="absolute inset-0 bg-teal-900/10 blur-[100px] -z-10 rounded-full"></div>
            <div class="flex flex-col gap-4 mt-12 overflow-hidden group">
              <img src="https://images.pexels.com/photos/1320686/pexels-photo-1320686.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-2/3 object-cover rounded-2xl shadow-2xl filter brightness-90 group-hover:brightness-110 group-hover:scale-105 transition-all duration-700 border border-white/10" alt="Resort" />
              <img src="https://images.pexels.com/photos/262897/pexels-photo-262897.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-1/3 object-cover rounded-2xl shadow-2xl filter brightness-90 group-hover:brightness-110 group-hover:scale-105 transition-all duration-700 delay-100 border border-white/10" alt="Cuisine" />
            </div>
            <div class="flex flex-col gap-4 mb-12 overflow-hidden group">
              <img src="https://images.pexels.com/photos/2569263/pexels-photo-2569263.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-1/3 object-cover rounded-2xl shadow-2xl filter brightness-90 group-hover:brightness-110 group-hover:scale-105 transition-all duration-700 delay-200 border border-white/10" alt="Helicopter View" />
              <img src="https://images.pexels.com/photos/2444403/pexels-photo-2444403.jpeg?auto=compress&cs=tinysrgb&w=800" class="w-full h-2/3 object-cover rounded-2xl shadow-2xl filter brightness-90 group-hover:brightness-110 group-hover:scale-105 transition-all duration-700 delay-300 border border-white/10" alt="Wildlife Safari" />
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- PREMIUM CINEMATIC SEPARATOR -->
    <section class="min-h-[50vh] md:min-h-[70vh] w-full bg-[#050505] relative flex flex-col justify-center items-center z-20 shadow-[0_0_100px_rgba(0,0,0,0.8)] border-t border-white/[0.05]">
      <!-- Deep subtle radial glow -->
      <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-teal-900/10 via-[#050505] to-[#050505]"></div>
      
      <div class="gs-reveal flex flex-col items-center relative z-10 w-full px-6">
        <div class="w-[1px] h-24 md:h-40 bg-gradient-to-b from-transparent via-teal-500/50 to-teal-500 mb-10 md:mb-16"></div>
        
        <h3 class="text-3xl md:text-5xl lg:text-[4.5rem] font-serif font-light text-center text-white/90 leading-[1.2] tracking-wide drop-shadow-2xl">
          We don't just curate itineraries.<br/>
          <span class="italic text-teal-400 font-medium mt-4 block">We orchestrate feeling.</span>
        </h3>
        
        <div class="w-[1px] h-24 md:h-40 bg-gradient-to-t from-transparent via-white/20 to-white mt-10 md:mb-0"></div>
      </div>
    </section>

    <!-- 6. THE EXPERIENCE — Promotional Showcase -->
    <section class="py-32 md:py-48 px-6 md:px-16 bg-[#030303] border-t border-white/5 relative overflow-hidden">
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom_left,_var(--tw-gradient-stops))] from-teal-900/15 via-[#030303] to-[#030303] pointer-events-none"></div>

      <div class="max-w-[1700px] mx-auto">
        <!-- Section Header -->
        <div class="gs-reveal flex flex-col md:flex-row md:items-end justify-between mb-24">
          <div>
            <span class="uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold flex items-center gap-4 mb-6 font-sans">
              <span class="w-8 h-[1px] bg-teal-500"></span>
              The Experience
            </span>
            <h2 class="text-5xl md:text-[6rem] font-serif font-medium leading-none tracking-tighter text-white drop-shadow-md">
              Every detail.<br/>
              <span class="italic font-light text-teal-300">Perfected.</span>
            </h2>
          </div>
          <p class="mt-8 md:mt-0 max-w-sm text-white/60 font-sans font-light text-sm md:text-base leading-relaxed md:border-l border-white/10 md:pl-6">
            From the moment you inquire to the final farewell at the airport, every touchpoint is handled with supreme care and total discretion.
          </p>
        </div>

        <!-- Feature Grid -->
        <div class="gs-reveal grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-px bg-white/5 border border-white/5 rounded-3xl overflow-hidden">

          <div class="group bg-[#050505] p-10 hover:bg-teal-900/20 transition-all duration-700 relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-teal-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            <div class="w-12 h-12 rounded-full border border-teal-500/30 flex items-center justify-center mb-8 group-hover:border-teal-500 transition-colors duration-500">
              <q-icon name="flight" size="sm" class="text-teal-500" />
            </div>
            <h4 class="text-xl font-serif font-light text-white mb-4">Seamless Transfers</h4>
            <p class="text-sm text-white/50 font-sans font-light leading-relaxed">Private aviation, helicopter charters, and luxury ground transfers — perfectly timed for zero friction.</p>
            <div class="mt-8 flex items-center gap-3 text-teal-500 text-[10px] uppercase tracking-[0.3em] font-bold font-sans opacity-0 group-hover:opacity-100 transition-opacity duration-500">
              <div class="w-4 h-[1px] bg-teal-500"></div>
              Included
            </div>
          </div>

          <div class="group bg-[#050505] p-10 hover:bg-teal-900/20 transition-all duration-700 relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-teal-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            <div class="w-12 h-12 rounded-full border border-teal-500/30 flex items-center justify-center mb-8 group-hover:border-teal-500 transition-colors duration-500">
              <q-icon name="villa" size="sm" class="text-teal-500" />
            </div>
            <h4 class="text-xl font-serif font-light text-white mb-4">Private Villas</h4>
            <p class="text-sm text-white/50 font-sans font-light leading-relaxed">Exclusive residences with dedicated butlers, cliff-edge infinity pools, and breathtaking ocean or jungle panoramas.</p>
            <div class="mt-8 flex items-center gap-3 text-teal-500 text-[10px] uppercase tracking-[0.3em] font-bold font-sans opacity-0 group-hover:opacity-100 transition-opacity duration-500">
              <div class="w-4 h-[1px] bg-teal-500"></div>
              Included
            </div>
          </div>

          <div class="group bg-[#050505] p-10 hover:bg-teal-900/20 transition-all duration-700 relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-teal-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            <div class="w-12 h-12 rounded-full border border-teal-500/30 flex items-center justify-center mb-8 group-hover:border-teal-500 transition-colors duration-500">
              <q-icon name="restaurant" size="sm" class="text-teal-500" />
            </div>
            <h4 class="text-xl font-serif font-light text-white mb-4">Private Chef</h4>
            <p class="text-sm text-white/50 font-sans font-light leading-relaxed">Personal chefs preparing multi-course fusion cuisine. Private candlelit dinners on beaches, on mountaintops, or within ancient temples.</p>
            <div class="mt-8 flex items-center gap-3 text-teal-500 text-[10px] uppercase tracking-[0.3em] font-bold font-sans opacity-0 group-hover:opacity-100 transition-opacity duration-500">
              <div class="w-4 h-[1px] bg-teal-500"></div>
              Included
            </div>
          </div>

          <div class="group bg-[#050505] p-10 hover:bg-teal-900/20 transition-all duration-700 relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-teal-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            <div class="w-12 h-12 rounded-full border border-teal-500/30 flex items-center justify-center mb-8 group-hover:border-teal-500 transition-colors duration-500">
              <q-icon name="health_and_safety" size="sm" class="text-teal-500" />
            </div>
            <h4 class="text-xl font-serif font-light text-white mb-4">Total Privacy</h4>
            <p class="text-sm text-white/50 font-sans font-light leading-relaxed">NDA-protected concierge service for heads of state, CEOs, and discerning families. Your stay remains completely confidential.</p>
            <div class="mt-8 flex items-center gap-3 text-teal-500 text-[10px] uppercase tracking-[0.3em] font-bold font-sans opacity-0 group-hover:opacity-100 transition-opacity duration-500">
              <div class="w-4 h-[1px] bg-teal-500"></div>
              Guaranteed
            </div>
          </div>

        </div>

        <!-- Large CTA Banner -->
        <div class="gs-reveal mt-px bg-white/[0.03] border border-white/5 rounded-3xl overflow-hidden mt-4">
          <div class="relative p-12 md:p-20 flex flex-col md:flex-row items-center justify-between gap-12">
            <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_left,_var(--tw-gradient-stops))] from-teal-900/20 via-transparent to-transparent pointer-events-none"></div>
            <div class="relative z-10">
              <h3 class="text-4xl md:text-6xl font-serif font-light text-white leading-tight mb-4">
                Ready to begin?<br/>
                <span class="italic text-teal-300">The island awaits.</span>
              </h3>
              <p class="text-white/50 font-sans font-light text-sm max-w-md">A dedicated travel architect will personally respond to your inquiry within 12 hours. All enquiries are held in the strictest confidence.</p>
            </div>
            <div class="relative z-10 flex flex-col gap-4 items-start md:items-end shrink-0">
              <button @click="contactModal = true; playClick()" class="group px-10 py-5 bg-white text-black font-sans uppercase font-bold tracking-[0.3em] text-[11px] hover:bg-teal-500 hover:text-white transition-all duration-500 shadow-[0_0_40px_rgba(255,255,255,0.15)] relative overflow-hidden">
                <span class="relative z-10">Begin Your Journey</span>
                <div class="absolute inset-0 bg-teal-600 transform scale-x-0 origin-left group-hover:scale-x-100 transition-transform duration-500 ease-out z-0"></div>
              </button>
              <span class="text-white/30 font-sans text-[10px] uppercase tracking-[0.2em]">No commitment required</span>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- 7. FOOTER -->
    <footer class="bg-[#030303] border-t border-white/10 relative overflow-hidden w-full">
      <!-- Cinematic Video Background -->
      <video autoplay loop muted playsinline class="absolute inset-0 w-full h-full object-cover opacity-20 filter grayscale contrast-[1.1] pointer-events-none z-0">
        <source src="https://www.shutterstock.com/shutterstock/videos/3784304231/preview/stock-footage-travel-and-exploration-of-tourist-woman-by-sri-lankan-train-in-second-class-wagon-to-famous-places.mp4" type="video/mp4" />
      </video>
      <div class="absolute inset-0 bg-gradient-to-t from-[#030303] via-[#030303]/85 to-[#030303]/60 pointer-events-none z-10"></div>

      <!-- Main Footer Content -->
      <div class="relative z-20 max-w-[1700px] mx-auto px-6 md:px-16 pt-32 pb-12">
        <!-- Awaken CTA -->
        <div class="text-center mb-32 gs-reveal">
          <span class="font-sans uppercase tracking-[0.5em] text-[10px] text-teal-400 font-bold block mb-8">Access the Unattainable</span>
          <h2 class="text-7xl md:text-[9rem] font-serif font-medium leading-none drop-shadow-2xl text-white tracking-tighter mb-12">Awaken.</h2>
          <button @click="contactModal = true; playClick()" class="group inline-flex items-center gap-6 px-12 py-5 bg-white text-black font-sans uppercase font-bold tracking-[0.3em] text-[11px] hover:bg-teal-500 hover:text-white transition-all duration-500 shadow-[0_0_40px_rgba(255,255,255,0.15)] relative overflow-hidden">
            <span class="relative z-10">Request Consultation</span>
            <div class="absolute inset-0 bg-teal-600 transform scale-x-0 origin-left group-hover:scale-x-100 transition-transform duration-500 ease-out z-0"></div>
          </button>
        </div>

        <!-- Footer Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-16 border-t border-white/10 pt-16">
          <!-- Brand -->
          <div>
            <div class="text-3xl font-black tracking-[0.3em] uppercase text-white mb-6">Seren<span class="text-teal-500 font-light">div</span>.</div>
            <p class="text-white/40 font-sans font-light text-xs leading-relaxed max-w-[200px]">Sri Lanka's most exclusive private travel design studio. Est. 2026.</p>
          </div>

          <!-- Navigate -->
          <div>
            <div class="text-[9px] uppercase tracking-[0.4em] text-teal-400 font-bold font-sans mb-8">Navigate</div>
            <div class="flex flex-col gap-4 font-sans">
              <a @click.prevent="scrollTo('#about')" class="text-white/50 hover:text-white text-sm cursor-pointer transition-colors">The Story</a>
              <a @click.prevent="scrollTo('#destinations')" class="text-white/50 hover:text-white text-sm cursor-pointer transition-colors">Destinations</a>
              <a @click.prevent="scrollTo('#concierge')" class="text-white/50 hover:text-white text-sm cursor-pointer transition-colors">Services</a>
              <router-link to="/journal" class="text-white/50 hover:text-white text-sm cursor-pointer transition-colors">Journal</router-link>
            </div>
          </div>

          <!-- Experiences -->
          <div>
            <div class="text-[9px] uppercase tracking-[0.4em] text-teal-400 font-bold font-sans mb-8">Experiences</div>
            <div class="flex flex-col gap-4 font-sans">
              <router-link to="/heritage" class="text-white/50 hover:text-white text-sm cursor-pointer transition-colors relative group flex items-center gap-3">
                <span class="w-0 h-[1px] bg-teal-500 group-hover:w-4 transition-all duration-300"></span>
                Heritage Journeys
              </router-link>
              <router-link to="/wildlife" class="text-white/50 hover:text-white text-sm cursor-pointer transition-colors relative group flex items-center gap-3">
                <span class="w-0 h-[1px] bg-teal-500 group-hover:w-4 transition-all duration-300"></span>
                Wildlife Safaris
              </router-link>
              <router-link to="/coastal" class="text-white/50 hover:text-white text-sm cursor-pointer transition-colors relative group flex items-center gap-3">
                <span class="w-0 h-[1px] bg-teal-500 group-hover:w-4 transition-all duration-300"></span>
                Coastal Retreats
              </router-link>
              <router-link to="/aviation" class="text-white/50 hover:text-white text-sm cursor-pointer transition-colors relative group flex items-center gap-3">
                <span class="w-0 h-[1px] bg-teal-500 group-hover:w-4 transition-all duration-300"></span>
                Private Aviation
              </router-link>
            </div>
          </div>

          <!-- Contact -->
          <div>
            <div class="text-[9px] uppercase tracking-[0.4em] text-teal-400 font-bold font-sans mb-8">Connect</div>
            <div class="flex flex-col gap-4 font-sans">
              <a href="https://www.instagram.com" target="_blank" class="text-white/50 hover:text-teal-400 text-sm transition-colors flex items-center gap-3">
                <q-icon name="photo_camera" size="xs"/> Instagram
              </a>
              <a href="mailto:inquire@serendiv.com" class="text-white/50 hover:text-teal-400 text-sm transition-colors flex items-center gap-3">
                <q-icon name="mail_outline" size="xs"/> inquire@serendiv.com
              </a>
              <a href="tel:+94000000000" class="text-white/50 hover:text-teal-400 text-sm transition-colors flex items-center gap-3">
                <q-icon name="phone" size="xs"/> +94 77 000 0000
              </a>
            </div>
          </div>
        </div>

        <!-- Bottom Legal Bar -->
        <div class="mt-16 pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between gap-6 font-sans text-[10px] tracking-[0.1em] text-white/30 uppercase">
          <div>© {{ new Date().getFullYear() }} Serendiv Immersive Ltd. All rights reserved.</div>
          <div class="flex gap-8">
            <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
            <a href="#" class="hover:text-white transition-colors">Terms of Use</a>
            <a href="#" class="hover:text-white transition-colors">Cookie Policy</a>
          </div>
        </div>
      </div>
    </footer>

    <!-- MODAL: DETAILED ITINERARY / VIEW -->
    <q-dialog v-model="destinationModal" maximized class="z-[100]">
      <div class="bg-[#050505] min-h-screen text-white flex font-sans w-full">
        <!-- Close Button -->
        <button @click="destinationModal = false" class="fixed top-8 right-8 z-50 w-12 h-12 bg-black/50 border border-white/20 rounded-full flex items-center justify-center hover:bg-white/20 transition-colors backdrop-blur-md">
          <q-icon name="close" size="xs" />
        </button>

        <!-- Left Image Panel -->
        <div class="hidden lg:block w-5/12 h-screen relative border-r border-white/10">
          <img :src="activeDestination?.imgFull || activeDestination?.img" class="absolute inset-0 w-full h-full object-cover filter brightness-90 shadow-[inset_0_0_100px_rgba(0,0,0,1)]" />
          <div class="absolute inset-0 bg-gradient-to-r from-transparent to-[#050505]"></div>
        </div>

        <!-- Right Content Panel -->
        <div class="w-full lg:w-7/12 h-screen overflow-y-auto px-6 py-24 md:px-20 relative bg-[#050505]">
          <div v-if="activeDestination" class="max-w-2xl animate-fade-in-up">
            <span class="uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold block mb-4">{{ activeDestination.tag }} — Curated Route</span>
            <h2 class="text-6xl md:text-[5rem] font-serif font-medium mb-8 leading-tight drop-shadow-md text-white">{{ activeDestination.title }}</h2>
            
            <!-- Image for mobile -->
            <img :src="activeDestination.img" class="w-full h-64 sm:h-80 md:h-96 object-cover my-10 lg:hidden rounded-xl border border-white/10 shadow-lg" />

            <!-- Long Description -->
            <div class="text-gray-300 font-light text-lg leading-relaxed space-y-6 mb-16 border-l-2 pl-6 border-teal-500/50 bg-white/5 p-6 rounded-r-xl shadow-inner">
              <p>{{ activeDestination.overview }}</p>
              <p>{{ activeDestination.details }}</p>
            </div>

            <!-- Features Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-10 border-t border-b border-white/10 py-10 mb-16 bg-black/20 px-8 rounded-lg mt-8">
              <div>
                <span class="text-[10px] uppercase tracking-[0.2em] text-gray-500 font-bold block mb-2">Aviation / Transit</span>
                <span class="text-lg text-white font-light block">Private Helicopter/SUV</span>
              </div>
              <div>
                <span class="text-[10px] uppercase tracking-[0.2em] text-gray-500 font-bold block mb-2">Climate Window</span>
                <span class="text-lg text-white font-light block">{{ activeDestination.season }}</span>
              </div>
              <div class="md:col-span-2">
                <span class="text-[10px] uppercase tracking-[0.2em] text-gray-500 font-bold block mb-2">Signature Experiences</span>
                <span class="text-lg text-white font-light block">{{ activeDestination.highlights }}</span>
              </div>
              <div>
                <span class="text-[10px] uppercase tracking-[0.2em] text-teal-500 font-bold block mb-2">Starting Pricing</span>
                <span class="text-lg text-white font-serif font-bold">$2,500 / Night</span>
              </div>
            </div>

            <button @click="contactModal = true; destinationModal = false" class="px-12 py-5 bg-teal-600 text-white border border-teal-600 hover:bg-transparent hover:text-teal-400 hover:border-teal-400 transition-all font-bold uppercase tracking-[0.2em] text-[11px] rounded-sm shadow-[0_0_20px_rgba(13,148,136,0.3)]">
              Include in Inquiry
            </button>
          </div>
        </div>
      </div>
    </q-dialog>

    <!-- MODAL: BESPOKE INQUIRY (Plan Trip) -->
    <q-dialog v-model="contactModal" position="right" maximized class="z-[100]">
      <div class="bg-[#080808] w-full md:w-[600px] h-full p-8 md:p-14 border-l border-white/10 flex flex-col font-sans shadow-[-20px_0_50px_rgba(0,0,0,0.5)]">
        <div class="flex justify-between items-center mb-16">
          <div class="font-serif text-3xl font-medium text-white">Inquiry.</div>
          <button @click="contactModal = false" class="w-10 h-10 border border-white/20 flex items-center justify-center hover:bg-white/10 rounded-full bg-black/50"><q-icon name="close" size="xs" /></button>
        </div>
        
        <p class="text-gray-400 mb-12 font-light text-sm tracking-wide leading-relaxed bg-white/5 p-4 rounded-lg border border-white/5">
          Our concierge architecture is designed for total privacy and luxury. Please leave your details and an experience architect will contact you within 12 hours.
        </p>
        
        <form @submit.prevent="submitInquiry" class="space-y-8 flex-grow">
          <div class="relative">
            <input type="text" required class="w-full bg-transparent border-b border-white/30 py-4 text-white font-light focus:outline-none focus:border-teal-500 transition-colors peer placeholder-transparent" id="name" placeholder="Name">
            <label for="name" class="absolute left-0 top-4 text-xs text-gray-500 uppercase tracking-[0.2em] transition-all peer-focus:-top-4 peer-focus:text-[10px] peer-focus:text-teal-500 peer-valid:-top-4 peer-valid:text-[10px] pointer-events-none">Full Name</label>
          </div>
          
          <div class="relative mt-8">
            <input type="email" required class="w-full bg-transparent border-b border-white/30 py-4 text-white font-light focus:outline-none focus:border-teal-500 transition-colors peer placeholder-transparent" id="email" placeholder="Email">
            <label for="email" class="absolute left-0 top-4 text-xs text-gray-500 uppercase tracking-[0.2em] transition-all peer-focus:-top-4 peer-focus:text-[10px] peer-focus:text-teal-500 peer-valid:-top-4 peer-valid:text-[10px] pointer-events-none">Private Email</label>
          </div>
          
          <div class="pt-6">
            <label class="block text-[10px] text-gray-400 uppercase tracking-[0.2em] mb-4 font-bold">Atmosphere Preference</label>
            <div class="grid grid-cols-2 gap-4">
              <label class="cursor-pointer">
                <input type="radio" name="preference" class="peer hidden" checked>
                <div class="border border-white/20 p-4 text-center peer-checked:border-teal-500 peer-checked:bg-teal-900/30 text-xs tracking-[0.2em] uppercase font-bold text-gray-400 peer-checked:text-teal-400 transition-all rounded-sm shadow-inner">Heritage</div>
              </label>
              <label class="cursor-pointer">
                <input type="radio" name="preference" class="peer hidden">
                <div class="border border-white/20 p-4 text-center peer-checked:border-teal-500 peer-checked:bg-teal-900/30 text-xs tracking-[0.2em] uppercase font-bold text-gray-400 peer-checked:text-teal-400 transition-all rounded-sm shadow-inner">Wild</div>
              </label>
            </div>
          </div>
          
          <button type="submit" class="w-full py-5 bg-teal-600 hover:bg-teal-500 text-white font-bold uppercase tracking-[0.3em] text-[10px] mt-12 transition-all flex items-center justify-center gap-4 group rounded-sm shadow-[0_0_20px_rgba(13,148,136,0.2)]" :disabled="isSubmitting">
            <span>{{ isSubmitting ? 'ENCRYPTING...' : 'SUBMIT INQUIRY' }}</span>
            <q-icon v-if="!isSubmitting" name="arrow_forward" size="xs" class="group-hover:translate-x-2 transition-transform" />
            <q-spinner v-else color="white" size="xs" />
          </button>
        </form>
      </div>
    </q-dialog>

  </q-page>
</template>

<script setup>
import { ref, onMounted, onUnmounted, nextTick, computed } from 'vue'
import * as THREE from 'three'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import Lenis from '@studio-freight/lenis'
import mapboxgl from 'mapbox-gl'
import 'mapbox-gl/dist/mapbox-gl.css'

gsap.registerPlugin(ScrollTrigger)

// Core Refs
const scrolled = ref(0)
const mobileMenu = ref(false)
const contactModal = ref(false)
const destinationModal = ref(false)
const activeDestination = ref(null)
const isSubmitting = ref(false)
const audioPlayer = ref(null)
const clickSound = ref(null)
const isAudioPlaying = ref(false)
const heroCanvas = ref(null)
const activeMapLocation = ref(null)
const mapVideoPreview = ref(null)
let lenis

// INTERACTIVE MAP DATA
let mapInstance = null // mapbox map reference
const mapLocations = [
  { name: 'Sigiriya', lng: 80.7510, lat: 7.9570, tag: 'UNESCO Heritage', desc: 'A colossal 5th-century rock fortress rising 200 metres from the jungle canopy. Ancient frescoes, mirror walls, and elaborate water gardens await at this 8th Wonder of the World.', video: 'https://www.shutterstock.com/shutterstock/videos/3796051381/preview/stock-footage-3796051381.mp4' },
  { name: 'Kandy', lng: 80.6366, lat: 7.2906, tag: 'Sacred City', desc: 'The last royal capital of Sri Lanka, cradled by misty hills. Home to the revered Temple of the Tooth Relic — the most venerated Buddhist shrine on Earth.', video: 'https://www.shutterstock.com/shutterstock/videos/3784304231/preview/stock-footage-travel-and-exploration-of-tourist-woman-by-sri-lankan-train-in-second-class-wagon-to-famous-places.mp4' },
  { name: 'Trincomalee', lng: 81.2335, lat: 8.5874, tag: 'East Coast Blues', desc: 'Pristine turquoise bays on the untouched east coast. Home to Pigeon Island, hot springs at Kanniyai, and the ancient Koneswaram Temple perched above the sea.', video: 'https://www.shutterstock.com/shutterstock/videos/3796732103/preview/stock-footage-breathtaking-aerial-view-mirissa-beach-parrot-rock.mp4' },
  { name: 'Nuwara Eliya', lng: 80.7829, lat: 6.9497, tag: 'Hill Country', desc: 'The "Little England" of Sri Lanka. Rolling emerald tea estates, colonial-era bungalows, and the world\'s most scenic highland train journey through cascading waterfalls.', video: 'https://www.shutterstock.com/shutterstock/videos/3784304231/preview/stock-footage-travel-and-exploration-of-tourist-woman-by-sri-lankan-train-in-second-class-wagon-to-famous-places.mp4' },
  { name: 'Yala', lng: 81.5034, lat: 6.2731, tag: 'Leopard Capital', desc: 'The highest density of leopards in the world. Golden-hour jeep safaris through lagoons, rocky outcrops, and vast open plains teeming with wildlife.', video: 'https://www.shutterstock.com/shutterstock/videos/3800595019/preview/stock-footage-a-powerful-portrait-of-an-asian-male-elephant-roaming-freely-in-miyamina-park-sri-lanka.mp4' },
  { name: 'Mirissa', lng: 80.4571, lat: 5.9483, tag: 'Ocean Paradise', desc: 'A golden crescent bay flanked by coconut palms. Private catamaran expeditions at dawn to witness majestic Blue Whales — the largest creatures ever to have lived.', video: 'https://www.shutterstock.com/shutterstock/videos/3796732103/preview/stock-footage-breathtaking-aerial-view-mirissa-beach-parrot-rock.mp4' },
  { name: 'Galle', lng: 80.2170, lat: 6.0328, tag: 'Colonial Heritage', desc: 'A living 16th-century Dutch fort where time stands still. Cobblestone streets, boutique galleries, and golden sunsets from 400-year-old ramparts above the Indian Ocean.', video: 'https://www.shutterstock.com/shutterstock/videos/3796732103/preview/stock-footage-breathtaking-aerial-view-mirissa-beach-parrot-rock.mp4' },
  { name: 'Arugam Bay', lng: 81.8315, lat: 6.8406, tag: 'Surf Capital', desc: 'One of the top ten surf points on Earth. A perfect moon-shaped bay backed by bohemian beach villas, warm emerald waters, and mesmerizing sunrises.', video: 'https://www.shutterstock.com/shutterstock/videos/3796732103/preview/stock-footage-breathtaking-aerial-view-mirissa-beach-parrot-rock.mp4' },
]

const openMapVideo = (loc) => {
  activeMapLocation.value = loc
  playClick()
  
  if (mapInstance && loc.lng && loc.lat) {
    mapInstance.flyTo({
      center: [loc.lng, loc.lat],
      zoom: 8.5,
      pitch: 45,
      bearing: 15,
      speed: 1.2,
      curve: 1.42,
      essential: true
    })
  }
}

const setupMapbox = () => {
  mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_ACCESS_TOKEN // Use env var provided in Vercel/local .env
  mapInstance = new mapboxgl.Map({
    container: 'mapbox-container',
    style: 'mapbox://styles/mapbox/dark-v11', // Premium dark style
    center: [80.7718, 7.5], // Center of Sri Lanka
    zoom: 7.2, // Zoomed in heavily for full island perspective
    pitch: 20,
    scrollZoom: true // Re-enabled scroll zoom
  })

  // Add zoom and rotation controls
  mapInstance.addControl(new mapboxgl.NavigationControl(), 'bottom-right')

  mapInstance.on('load', () => {
    // Add custom HTML markers
    mapLocations.forEach((loc, index) => {
      // Create element
      const el = document.createElement('div')
      el.className = 'custom-map-marker'
      el.innerHTML = `
        <div class="map-ping" style="animation-delay: ${index * 0.3}s"></div>
        <div class="map-dot"></div>
        <div class="map-label">${loc.name}</div>
      `
      
      el.addEventListener('click', () => {
        openMapVideo(loc)
      })
      el.addEventListener('mouseenter', () => {
        el.classList.add('active-marker')
      })
      el.addEventListener('mouseleave', () => {
        el.classList.remove('active-marker')
      })

      // Attach marker with exact center anchoring
      new mapboxgl.Marker({ element: el, anchor: 'center' })
        .setLngLat([loc.lng, loc.lat])
        .addTo(mapInstance)
    })
    
    // Fix Mapbox resizing bug
    const mapContainerElement = document.getElementById('mapbox-container')
    if (mapContainerElement) {
      new ResizeObserver(() => {
        mapInstance.resize()
      }).observe(mapContainerElement)
    }
  })
}

const playMapVideo = () => {
  // Open in fullscreen overlay or just play inline
  if (mapVideoPreview.value) {
    mapVideoPreview.value.muted = false
    mapVideoPreview.value.volume = 0.5
    mapVideoPreview.value.play().catch(() => {})
  }
}

// SOUNDS
const playClick = () => {
  if(clickSound.value) {
    clickSound.value.currentTime = 0;
    clickSound.value.volume = 0.2;
    clickSound.value.play().catch(()=> { /* ignore error */})
  }
}

// THE AURA VIBES ENGINE (Images only)
const vibes = [
  {
    id: 'ancient',
    name: 'Heritage',
    description: 'Step into an ancient world of untouched regality. From the cloud-kissed monolithic fortress of Sigiriya to the deeply sacred sanctuaries of Kandy, uncover the timeless mysteries of a 2,500-year-old civilization.',
    audio: 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Singing_bowl_1.ogg', 
    color: 0xffaa44 
  },
  {
    id: 'wild',
    name: 'Wildlife',
    description: 'A raw, uncompromising immersion into the kingdom of the wild. Lock eyes with the elusive Sri Lankan leopard, traverse terrain with nomadic elephants, and track majestic blue whales across the sapphire deep.',
    audio: 'https://upload.wikimedia.org/wikipedia/commons/e/e0/Jungle_atmosphere.ogg',
    color: 0x22ff88 
  },
  {
    id: 'serene',
    name: 'Coastal Retreat',
    description: 'Surrender to the unbroken rhythm of the Indian Ocean. Exclusive, sun-drenched private villas set against pristine golden sands, where edge-of-the-world surfing meets unadulterated, pure serenity.',
    audio: 'https://upload.wikimedia.org/wikipedia/commons/0/07/Ocean_Waves.ogg',
    color: 0x44ccff 
  }
]
const activeVibeIndex = ref(0)
const currentVibe = ref(vibes[0])

const setVibe = (vibe, index) => {
  if (currentVibe.value.id === vibe.id) return
  playClick()
  activeVibeIndex.value = index
  currentVibe.value = vibe
  
  isAudioPlaying.value = true
  if (audioPlayer.value) {
    audioPlayer.value.pause()
    audioPlayer.value.src = vibe.audio
    audioPlayer.value.load()
    audioPlayer.value.volume = 0.5
    audioPlayer.value.play().catch(() => {})
  }
  
  if(particleMaterial) {
    gsap.to(particleMaterial.color, {
      r: new THREE.Color(vibe.color).r,
      g: new THREE.Color(vibe.color).g,
      b: new THREE.Color(vibe.color).b,
      duration: 1.5
    })
  }

  gsap.fromTo('.vibe-desc-fade', {opacity: 0, y: 10}, {opacity: 1, y: 0, duration: 1})
}

const toggleAudio = () => {
  if (!audioPlayer.value) return
  if (isAudioPlaying.value) {
    audioPlayer.value.pause()
    isAudioPlaying.value = false
  } else {
    audioPlayer.value.volume = 0.4
    audioPlayer.value.play().catch(() => {})
    isAudioPlaying.value = true
  }
}

// DESTINATIONS DB
const destinations = [
  // --- ANCIENT (HERITAGE) ---
  {
    id: 'sigiriya',
    title: 'Sigiriya Rock Fortress',
    tag: 'Cultural Triangle',
    img: 'https://images.pexels.com/photos/2165074/pexels-photo-2165074.jpeg?auto=compress&cs=tinysrgb&w=1200',
    imgFull: 'https://images.pexels.com/photos/2165074/pexels-photo-2165074.jpeg?auto=compress&cs=tinysrgb&w=2000',
    overview: 'The spectacular "Lion Rock" is an 8th Wonder of the World. A massive column of rock nearly 200 meters high.',
    details: 'Climb the 1,200 steps to the summit, passing the magnificent Water Gardens and the incredibly well-preserved heavenly maiden frescoes.',
    season: 'January to April',
    highlights: 'Ancient Frescoes, Water Gardens',
    vibes: ['ancient']
  },
  {
    id: 'kandy',
    title: 'The Sacred City of Kandy',
    tag: 'Hill Capital',
    img: 'https://images.pexels.com/photos/10006798/pexels-photo-10006798.jpeg?auto=compress&cs=tinysrgb&w=1200',
    imgFull: 'https://images.pexels.com/photos/10006798/pexels-photo-10006798.jpeg?auto=compress&cs=tinysrgb&w=2000',
    overview: 'Sri Lanka’s cultural capital and the last stronghold of the Sinhalese Kings, set around a scenic lake.',
    details: 'Home to the Temple of the Sacred Tooth Relic. Experience traditional Kandyan dance performances and stroll through the Royal Botanical Gardens.',
    season: 'December to May',
    highlights: 'Temple of the Tooth, Botanical Gardens',
    vibes: ['ancient']
  },
  {
    id: 'polonnaruwa',
    title: 'Polonnaruwa Ancient City',
    tag: 'Medieval Capital',
    img: 'https://images.pexels.com/photos/1320686/pexels-photo-1320686.jpeg?auto=compress&cs=tinysrgb&w=1200',
    imgFull: 'https://images.pexels.com/photos/1320686/pexels-photo-1320686.jpeg?auto=compress&cs=tinysrgb&w=2000',
    overview: 'The second most ancient of Sri Lanka’s kingdoms, boasting towering stupas and gigantic rock sculptures.',
    details: 'Cycle through the ancient ruins at dawn. Discover the magnificent Gal Vihara, featuring four massive Buddha statues carved perfectly into a single granite rock face.',
    season: 'July to September',
    highlights: 'Gal Vihara, Parakrama Samudra',
    vibes: ['ancient']
  },
  {
    id: 'anuradhapura',
    title: 'Sacred Anuradhapura',
    tag: 'First Kingdom',
    img: 'https://images.pexels.com/photos/3389817/pexels-photo-3389817.jpeg?auto=compress&cs=tinysrgb&w=1200',
    imgFull: 'https://images.pexels.com/photos/3389817/pexels-photo-3389817.jpeg?auto=compress&cs=tinysrgb&w=2000',
    overview: 'The greatest monastic city of the ancient world. Established in 377 BC, spreading over an immense area.',
    details: 'Pay homage to the Jaya Sri Maha Bodhi, the oldest historically documented tree on earth. Witness towering brick stupas glowing under the moon.',
    season: 'April to September',
    highlights: 'Jaya Sri Maha Bodhi, Ruwanwelisaya',
    vibes: ['ancient']
  },
  {
    id: 'dambulla',
    title: 'Dambulla Cave Temples',
    tag: 'Rock Monasteries',
    img: 'https://images.pexels.com/photos/2165074/pexels-photo-2165074.jpeg?auto=compress&cs=tinysrgb&w=1200&flip=h&crop=edges',
    imgFull: 'https://images.pexels.com/photos/2165074/pexels-photo-2165074.jpeg?auto=compress&cs=tinysrgb&w=2000&flip=h&crop=edges',
    overview: 'The largest and best-preserved cave temple complex in Sri Lanka, packed with Buddhist murals and 157 statues.',
    details: 'Five separate caves dug into a 160-meter rock. The ceiling murals trace the life of Lord Buddha, painted intricately centuries ago and preserved under natural stone.',
    season: 'Year-round',
    highlights: 'Golden Temple, 157 Buddha Statues',
    vibes: ['ancient']
  },
  {
    id: 'yapahuwa',
    title: 'Yapahuwa Rock Citadel',
    tag: 'Hidden Fortress',
    img: 'https://images.pexels.com/photos/10006798/pexels-photo-10006798.jpeg?auto=compress&cs=tinysrgb&w=1200&flip=v&bri=-10',
    imgFull: 'https://images.pexels.com/photos/10006798/pexels-photo-10006798.jpeg?auto=compress&cs=tinysrgb&w=2000&flip=v&bri=-10',
    overview: 'Rising almost 100 meters above the plains, this rock fortress served as the brief capital of Sri Lanka in the 13th century.',
    details: 'Climb the steep, beautifully ornamented staircase flanked by magnificent stone lions. This hidden gem offers a quiet, uncrowded exploration of ancient military architecture.',
    season: 'January to April',
    highlights: 'Ornamental Stairway, Stone Lions',
    vibes: ['ancient']
  },

  // --- WILD (WILDLIFE) ---
  {
    id: 'yala',
    title: 'Yala National Park',
    tag: 'Wildlife Safari',
    img: 'https://images.pexels.com/photos/1598377/pexels-photo-1598377.jpeg?auto=compress&cs=tinysrgb&w=1200',
    imgFull: 'https://images.pexels.com/photos/1598377/pexels-photo-1598377.jpeg?auto=compress&cs=tinysrgb&w=2000',
    overview: 'Sri Lanka’s premier wildlife destination, boasting one of the highest leopard densities in the world.',
    details: 'Embark on early morning 4x4 safaris across diverse terrains ranging from dense scrub jungle to coastal lagoons. Keep an eye out for majestic tuskers and slot bears.',
    season: 'February to July',
    highlights: 'Leopard Spotting, Luxury Tented Camps',
    vibes: ['wild']
  },
  {
    id: 'minneriya',
    title: 'Minneriya Elephant Gathering',
    tag: 'The Great Migration',
    img: 'https://images.pexels.com/photos/1598377/pexels-photo-1598377.jpeg?auto=compress&cs=tinysrgb&w=1200&crop=faces&fit=crop',
    imgFull: 'https://images.pexels.com/photos/1598377/pexels-photo-1598377.jpeg?auto=compress&cs=tinysrgb&w=2000&crop=faces&fit=crop',
    overview: 'Home to the largest known meeting place of Asian Elephants in the world.',
    details: 'During the dry season, hundreds of wild elephants gather around the ancient Minneriya reservoir. Witnessing this massive congregation is a once-in-a-lifetime wildlife spectacle.',
    season: 'July to October',
    highlights: 'Elephant Herds, Reservoir Views',
    vibes: ['wild']
  },
  {
    id: 'udawalawe',
    title: 'Udawalawe Sanctuary',
    tag: 'Wild Herds',
    img: 'https://images.pexels.com/photos/2569263/pexels-photo-2569263.jpeg?auto=compress&cs=tinysrgb&w=1200',
    imgFull: 'https://images.pexels.com/photos/2569263/pexels-photo-2569263.jpeg?auto=compress&cs=tinysrgb&w=2000',
    overview: 'A vast expanse of grasslands and waterholes, closely resembling the East African savannas.',
    details: 'Renowned for its large elephant population allowing for guaranteed sightings. Includes visits to the Elephant Transit Home where orphaned calves are rehabilitated.',
    season: 'October to May',
    highlights: 'Guaranteed Elephants, Orphanage',
    vibes: ['wild']
  },
  {
    id: 'sinharaja',
    title: 'Sinharaja Rain Forest',
    tag: 'Endemic Biodiversity',
    img: 'https://images.pexels.com/photos/3362489/pexels-photo-3362489.jpeg?auto=compress&cs=tinysrgb&w=1200',
    imgFull: 'https://images.pexels.com/photos/3362489/pexels-photo-3362489.jpeg?auto=compress&cs=tinysrgb&w=2000',
    overview: 'A UNESCO Biosphere Reserve and the last viable area of primary tropical rainforest in Sri Lanka.',
    details: 'Over 60% of the trees are endemic. A paradise for bird watchers and nature photographers. Guided treks reveal incredibly rare insects and amphibians.',
    season: 'August to September',
    highlights: 'Endemic Birds, Primary Rainforest',
    vibes: ['wild']
  },
  {
    id: 'wilpattu',
    title: 'Wilpattu National Park',
    tag: 'Untouched Wilderness',
    img: 'https://images.pexels.com/photos/1598377/pexels-photo-1598377.jpeg?auto=compress&cs=tinysrgb&w=1200&flip=h',
    imgFull: 'https://images.pexels.com/photos/1598377/pexels-photo-1598377.jpeg?auto=compress&cs=tinysrgb&w=2000&flip=h',
    overview: 'Sri Lanka’s largest and oldest national park, characterized by its unique "Villus".',
    details: 'A dense, quiet leopard reserve avoiding the mass crowds of Yala. The park is surrounded by copper-red soil and ancient archaeological ruins hidden within the thick jungle.',
    season: 'May to September',
    highlights: 'Silent Safaris, Villu Basins',
    vibes: ['wild']
  },
  {
    id: 'horton',
    title: 'Horton Plains & World\'s End',
    tag: 'Cloud Forests',
    img: 'https://images.pexels.com/photos/3362489/pexels-photo-3362489.jpeg?auto=compress&cs=tinysrgb&w=1200&flip=h&bri=20',
    imgFull: 'https://images.pexels.com/photos/3362489/pexels-photo-3362489.jpeg?auto=compress&cs=tinysrgb&w=2000&flip=h&bri=20',
    overview: 'A majestic high-altitude plateau covered by wild grasslands, cloud forests, and roaming Sambar deer.',
    details: 'Hike to the legendary "World\'s End" sheer drop and the magnificent Baker\'s Falls. The temperature drops drastically here, offering a unique alpine-like experience.',
    season: 'January to March',
    highlights: 'World\'s End Cliff, Baker\'s Falls',
    vibes: ['wild']
  },

  // --- SERENE (COASTAL RETREAT) ---
  {
    id: 'galle',
    title: 'Galle Fort Enclave',
    tag: 'Colonial Heritage / Coast',
    img: 'https://images.pexels.com/photos/3389817/pexels-photo-3389817.jpeg?auto=compress&cs=tinysrgb&w=1200&con=10',
    imgFull: 'https://images.pexels.com/photos/3389817/pexels-photo-3389817.jpeg?auto=compress&cs=tinysrgb&w=2000&con=10',
    overview: 'A living 16th-century Dutch fort where time stands still, bordered by the spectacular turquoise waters of the southern coast.',
    details: 'Wander the narrow cobblestone streets lined with boutique cafes, art galleries, and restored colonial villas. Drink in the golden sunset from the historic fort ramparts.',
    season: 'November to April',
    highlights: 'Fort Ramparts Walk, Boutique Shopping',
    vibes: ['serene']
  },
  {
    id: 'mirissa',
    title: 'Mirissa & Whale Watching',
    tag: 'Ocean Paradise',
    img: 'https://images.pexels.com/photos/2444403/pexels-photo-2444403.jpeg?auto=compress&cs=tinysrgb&w=1200',
    imgFull: 'https://images.pexels.com/photos/2444403/pexels-photo-2444403.jpeg?auto=compress&cs=tinysrgb&w=2000',
    overview: 'A vibrant coastal town famous for golden bays, surfing, and the world-class phenomena of Blue Whale migrations.',
    details: 'Set sail at dawn on a private yacht to witness the majesty of Blue Whales and Spinner Dolphins in their natural habitat.',
    season: 'November to April',
    highlights: 'Blue Whale Watching, Coconut Tree Hill',
    vibes: ['serene']
  },
  {
    id: 'bentota',
    title: 'Bentota Golden Beach',
    tag: 'Tropical Relaxation',
    img: 'https://images.pexels.com/photos/262897/pexels-photo-262897.jpeg?auto=compress&cs=tinysrgb&w=1200',
    imgFull: 'https://images.pexels.com/photos/262897/pexels-photo-262897.jpeg?auto=compress&cs=tinysrgb&w=2000',
    overview: 'A prime beach resort town characterized by luxury hotels framing a massive stretch of golden sand.',
    details: 'Relax under swaying palms or enjoy water sports on the Bentota River. End your day with a private, fine-dining seafood dinner directly on the sandy shores.',
    season: 'October to April',
    highlights: 'River Safari, Jet Skiing, Beach Dining',
    vibes: ['serene']
  },
  {
    id: 'arugambay',
    title: 'Arugam Bay Surf Coast',
    tag: 'Surf Capital',
    img: 'https://images.pexels.com/photos/2444403/pexels-photo-2444403.jpeg?auto=compress&cs=tinysrgb&w=1200&flip=h',
    imgFull: 'https://images.pexels.com/photos/2444403/pexels-photo-2444403.jpeg?auto=compress&cs=tinysrgb&w=2000&flip=h',
    overview: 'Counted among the top ten surf points in the world. A beautiful moon-shaped curl of soft sand.',
    details: 'Catch world-class waves during the day, and relax in bohemian luxury beach cafes at night. The surrounding area features quiet lagoons full of birdlife and wild elephants.',
    season: 'May to September',
    highlights: 'World-Class Surfing, Bohemian Cafes',
    vibes: ['serene']
  },
  {
    id: 'trinco',
    title: 'Trincomalee & Nilaveli',
    tag: 'East Coast Blues',
    img: 'https://images.pexels.com/photos/2444403/pexels-photo-2444403.jpeg?auto=compress&cs=tinysrgb&w=1200&sat=-40&con=20',
    imgFull: 'https://images.pexels.com/photos/2444403/pexels-photo-2444403.jpeg?auto=compress&cs=tinysrgb&w=2000&sat=-40&con=20',
    overview: 'The unspoiled eastern coast, featuring the impossibly white sands of Nilaveli and Uppuveli beaches.',
    details: 'Take a boat to Pigeon Island for unparalleled snorkeling over vibrant coral reefs. Visit the ancient Koneswaram Temple set spectacularly on a cliff overlooking the ocean.',
    season: 'May to October',
    highlights: 'Pigeon Island Snorkeling, Koneswaram',
    vibes: ['serene']
  },
  {
    id: 'tangalle',
    title: 'Tangalle Hidden Coves',
    tag: 'Secluded Luxury',
    img: 'https://images.pexels.com/photos/1320686/pexels-photo-1320686.jpeg?auto=compress&cs=tinysrgb&w=1200&flip=h',
    imgFull: 'https://images.pexels.com/photos/1320686/pexels-photo-1320686.jpeg?auto=compress&cs=tinysrgb&w=2000&flip=h',
    overview: 'Known for its series of rocky coves, massive crashing waves, and untouched sandy strips offering complete privacy.',
    details: 'Hide away in high-end, cliffside retreats. At night, witness giant marine turtles coming ashore to lay their eggs at the nearby Rekawa conservation project.',
    season: 'December to April',
    highlights: 'Private Coves, Cliffside Retreats',
    vibes: ['serene']
  }
]

const filteredDestinations = computed(() => {
  return destinations.filter(dest => dest.vibes.includes(currentVibe.value.id))
})

const openModal = (dest) => {
  activeDestination.value = dest
  destinationModal.value = true
  setTimeout(()=> {
    gsap.fromTo('.animate-fade-in-up', {opacity: 0, y: 30}, {opacity: 1, y: 0, duration: 1, ease: 'power3.out'})
  }, 100)
}

// Scrolling System
const scrollTo = (hash) => {
  const el = document.querySelector(hash)
  if (el && lenis) {
    lenis.scrollTo(el, { offset: 0, duration: 2, easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)) })
  }
}

// Form logic
const submitInquiry = () => {
  isSubmitting.value = true
  setTimeout(() => {
    isSubmitting.value = false
    contactModal.value = false
  }, 2000)
}

// -----------------------------------------
// WEBGL PARTICLES SYSTEM
// -----------------------------------------
let scene, camera, renderer, particleMaterial, particleSystem
let animFrameId
let pointerX = 0, pointerY = 0

const initWebGlEngine = () => {
  if (!heroCanvas.value) return
  
  scene = new THREE.Scene()
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
  camera.position.z = 30

  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true })
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5)) 
  heroCanvas.value.appendChild(renderer.domElement)

  const geom = new THREE.BufferGeometry()
  const count = 1000
  const pos = new Float32Array(count * 3)

  for(let i=0; i<count*3; i++){
    pos[i] = (Math.random() - 0.5) * 100 
  }

  geom.setAttribute('position', new THREE.BufferAttribute(pos, 3))
  particleMaterial = new THREE.PointsMaterial({
    size: 0.15,
    color: currentVibe.value.color,
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending,
  })

  particleSystem = new THREE.Points(geom, particleMaterial)
  scene.add(particleSystem)

  document.addEventListener('mousemove', (e) => {
    pointerX = (e.clientX - window.innerWidth / 2) * 0.01
    pointerY = (e.clientY - window.innerHeight / 2) * 0.01
  })
  
  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.setSize(window.innerWidth, window.innerHeight)
  })

  const renderLoop = () => {
    animFrameId = requestAnimationFrame(renderLoop)
    particleSystem.rotation.y += 0.0003
    particleSystem.rotation.x += 0.0001
    particleSystem.position.x += (pointerX - particleSystem.position.x) * 0.05
    particleSystem.position.y += (-pointerY - particleSystem.position.y) * 0.05
    renderer.render(scene, camera)
  }
  renderLoop()
}

// -----------------------------------------
// GSAP & LENIS INIT
// -----------------------------------------
onMounted(() => {
  nextTick(() => {
    lenis = new Lenis({
      duration: 1.5,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
      smoothWheel: true,
    })
    lenis.on('scroll', ScrollTrigger.update)
    lenis.on('scroll', (e) => { scrolled.value = e.animatedScroll })
    gsap.ticker.add((time) => { lenis.raf(time * 1000) })
    gsap.ticker.lagSmoothing(0)

    initWebGlEngine()
    setupMapbox()

    gsap.to('.hero-title .block', 
      { y: 0, duration: 1.5, ease: 'power4.out', stagger: 0.15, delay: 0.2 }
    )
    gsap.to('.hero-subtitle', 
      { opacity: 1, x: 0, duration: 1.5, ease: 'power4.out', delay: 0.8, startAt: { x: -30 } }
    )
    gsap.to('.hero-desc', 
      { opacity: 1, y: 0, duration: 1.5, ease: 'power4.out', delay: 1, startAt: { y: 20 } }
    )

    gsap.utils.toArray('.gs-reveal').forEach(el => {
      gsap.fromTo(el, 
        { y: 60, opacity: 0 }, 
        { 
          y: 0, opacity: 1, duration: 1.2, ease: 'cubic-bezier(0.25, 1, 0.5, 1)',
          scrollTrigger: { trigger: el, start: 'top 85%' }
        }
      )
    })
  })
})

onUnmounted(() => {
  if (lenis) lenis.destroy()
  if (animFrameId) cancelAnimationFrame(animFrameId)
  if (renderer) renderer.dispose()
})
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Inter:wght@300;400;600;700&display=swap');

html, body {
  background-color: #030303;
  color: white;
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.font-serif {
  font-family: 'Playfair Display', serif;
}
.font-sans, .q-page {
  font-family: 'Inter', sans-serif;
}

::selection { background: #0f766e; color: white; }
::-webkit-scrollbar { display: none; }
html { scrollbar-width: none; }

.animate-slide-up-slow {
  animation: slideUp 1.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes slideUp {
  0% { transform: translateY(100%); opacity: 0; }
  100% { transform: translateY(0); opacity: 1; }
}

.dest-list-move,
.dest-list-enter-active,
.dest-list-leave-active {
  transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}
.dest-list-enter-from,
.dest-list-leave-to {
  opacity: 0;
  transform: translateY(30px) scale(0.95);
}
.dest-list-leave-active {
  position: absolute;
}

.vibe-text-enter-active,
.vibe-text-leave-active {
  transition: all 0.7s cubic-bezier(0.25, 1, 0.5, 1);
}
.vibe-text-enter-from {
  opacity: 0;
  transform: translateY(15px);
  filter: blur(4px);
}
.vibe-text-leave-to {
  opacity: 0;
  transform: translateY(-15px);
  filter: blur(4px);
}

/* Map Animations */
.custom-map-marker {
  position: relative;
  width: 24px;
  height: 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

.map-dot {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 6px;
  height: 6px;
  background-color: #14b8a6;
  border-radius: 50%;
  box-shadow: 0 0 10px rgba(20, 184, 166, 0.8);
  transition: all 0.3s ease;
}

.map-ping {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 24px;
  height: 24px;
  border: 1px solid rgba(20, 184, 166, 0.5);
  border-radius: 50%;
  animation: mapPing 2s cubic-bezier(0, 0, 0.2, 1) infinite;
}

.map-label {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  margin-top: 8px;
  color: rgba(255, 255, 255, 0.6);
  font-family: 'Inter', sans-serif;
  font-size: 10px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  white-space: nowrap;
  opacity: 0.6;
  transition: all 0.3s ease;
  pointer-events: none;
}

.custom-map-marker:hover .map-dot,
.custom-map-marker.active-marker .map-dot {
  background-color: white;
  transform: translate(-50%, -50%) scale(1.5);
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.8);
}

.custom-map-marker:hover .map-label,
.custom-map-marker.active-marker .map-label {
  color: #14b8a6;
  opacity: 1;
  font-weight: 700;
  transform: translateX(-50%) translateY(2px);
}

@keyframes mapPing {
  0% { transform: translate(-50%, -50%) scale(0.5); opacity: 1; border-width: 1px; }
  100% { transform: translate(-50%, -50%) scale(2.5); opacity: 0; border-width: 0px; }
}
</style>
