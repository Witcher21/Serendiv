<template>
  <q-page class="bg-[#030303] text-white relative w-full min-h-screen font-serif flex flex-col items-center justify-center">
    
    <!-- Video Background -->
    <video autoplay loop muted playsinline class="absolute inset-0 w-full h-full object-cover opacity-30 filter grayscale-[30%] contrast-[1.2] pointer-events-none z-0">
      <source src="https://www.shutterstock.com/shutterstock/videos/3796732103/preview/stock-footage-3796732103.mp4" type="video/mp4" />
    </video>
    <div class="absolute inset-0 bg-gradient-to-b from-[#030303]/90 via-[#030303]/40 to-[#030303] pointer-events-none z-10"></div>

    <!-- Navigation -->
    <nav class="absolute top-0 w-full z-50 px-6 py-8 md:px-16 flex justify-between items-center font-sans tracking-[0.2em] uppercase text-xs">
      <router-link to="/" class="text-white hover:text-teal-400 transition-colors flex items-center gap-3 group">
        <q-icon name="arrow_back" size="sm" class="group-hover:-translate-x-1 transition-transform" />
        Return to Journey
      </router-link>
      <div class="text-xl md:text-2xl font-black tracking-[0.3em] text-white select-none">
        Seren<span class="text-teal-500 font-light">div</span>.
      </div>
    </nav>

    <!-- Content -->
    <div class="relative z-20 text-center max-w-4xl mx-auto px-6 mt-20">
      <span class="font-sans uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold block mb-8 animate-fade-in-up">The Journal — Chapter I</span>
      <h1 class="text-6xl md:text-[6rem] font-medium leading-[1.1] mb-12 drop-shadow-2xl animate-fade-in-up" style="animation-delay: 0.2s">
        The Highland <br/> <span class="italic font-light text-gray-400">Odyssey.</span>
      </h1>
      <p class="font-sans font-light text-gray-300 text-lg md:text-xl leading-relaxed max-w-2xl mx-auto animate-fade-in-up" style="animation-delay: 0.4s">
        A documented journey through the emerald heart of Sri Lanka. From the world’s most scenic railway routes to the undiscovered mountain passes of the tea country, read the field notes of our experience architects.
      </p>

      <div class="mt-20 font-sans animate-fade-in-up" style="animation-delay: 0.6s">
        <button class="px-12 py-5 bg-transparent border border-white text-white font-bold uppercase tracking-[0.3em] text-[10px] hover:bg-white hover:text-black transition-all duration-500 rounded-sm">
          Read Chapter
        </button>
      </div>
    </div>
  </q-page>
</template>

<style scoped>
.font-sans { font-family: 'Inter', sans-serif; }
.font-serif { font-family: 'Playfair Display', serif; }

.animate-fade-in-up {
  opacity: 0;
  animation: fadeInUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
