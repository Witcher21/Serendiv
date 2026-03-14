<template>
  <q-page class="bg-[#030303] text-white relative w-full min-h-screen font-serif">

    <!-- Cinematic Video Background -->
    <video autoplay loop muted playsinline class="fixed inset-0 w-full h-full object-cover opacity-40 filter contrast-[1.1] pointer-events-none z-0">
      <source src="https://www.shutterstock.com/shutterstock/videos/3784304231/preview/stock-footage-travel-and-exploration-of-tourist-woman-by-sri-lankan-train-in-second-class-wagon-to-famous-places.mp4" type="video/mp4" />
    </video>
    <div class="fixed inset-0 bg-gradient-to-b from-[#030303]/80 via-[#030303]/20 to-[#030303]/95 pointer-events-none z-10"></div>

    <!-- Navigation -->
    <nav class="fixed top-0 w-full z-50 px-6 py-8 md:px-16 flex justify-between items-center font-sans tracking-[0.2em] uppercase text-xs">
      <router-link to="/" class="text-white hover:text-teal-400 transition-colors flex items-center gap-3 group">
        <q-icon name="arrow_back" size="sm" class="group-hover:-translate-x-1 transition-transform" />
        Return to Journey
      </router-link>
      <div class="text-xl md:text-2xl font-black tracking-[0.3em] text-white select-none">
        Seren<span class="text-teal-500 font-light">div</span>.
      </div>
    </nav>

    <!-- Hero -->
    <section class="relative z-20 min-h-screen flex flex-col justify-center px-6 md:px-16 pt-32">
      <div class="max-w-[1400px] mx-auto w-full">
        <span class="font-sans uppercase tracking-[0.5em] text-[10px] text-teal-400 font-bold flex items-center gap-6 mb-10 animate-fade-in-up">
          <span class="w-12 h-[1px] bg-teal-500"></span>
          Private Aviation — Above the Island
        </span>
        <h1 class="text-[4rem] sm:text-[5rem] md:text-[7rem] font-medium leading-[1] tracking-tighter drop-shadow-2xl mb-12 animate-fade-in-up" style="animation-delay:0.2s">
          Above<br/>
          <span class="italic font-light text-teal-300">Everything.</span>
        </h1>
        <div class="border-l-2 border-teal-500/50 pl-8 max-w-xl animate-fade-in-up" style="animation-delay:0.4s">
          <p class="font-sans font-light text-white/80 text-base md:text-lg leading-[2]">
            Traverse the entire island in a single afternoon. Our private helicopter and charter flight services lift you above traffic, time, and the ordinary — delivering you to Sri Lanka's most remote and spectacular corners in absolute style.
          </p>
        </div>
        <div class="mt-16 flex flex-col sm:flex-row gap-6 animate-fade-in-up" style="animation-delay:0.6s">
          <router-link to="/" class="group px-10 py-5 bg-white text-black font-sans uppercase font-bold tracking-[0.3em] text-[11px] hover:bg-teal-500 hover:text-white transition-all duration-500 relative overflow-hidden inline-flex items-center gap-4">
            <span class="relative z-10">Request Aviation</span>
            <div class="absolute inset-0 bg-teal-600 transform scale-x-0 origin-left group-hover:scale-x-100 transition-transform duration-500 ease-out z-0"></div>
          </router-link>
          <router-link to="/" class="px-10 py-5 border border-white/30 text-white font-sans uppercase font-bold tracking-[0.3em] text-[11px] hover:border-teal-500 hover:text-teal-400 transition-all duration-500 inline-flex items-center gap-4">
            View All Services
          </router-link>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section class="relative z-20 py-32 px-6 md:px-16 bg-[#030303]/80 backdrop-blur-sm">
      <div class="max-w-[1400px] mx-auto">
        <div class="flex items-center gap-6 mb-20 font-sans">
          <div class="w-12 h-[1px] bg-teal-500"></div>
          <span class="uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold">Aviation Portfolio</span>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-px bg-white/5 border border-white/5 rounded-3xl overflow-hidden">
          <div v-for="service in services" :key="service.name" class="group bg-[#050505] p-10 hover:bg-teal-900/20 transition-all duration-700 relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-teal-500/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-700"></div>
            <div class="w-14 h-14 rounded-full border border-teal-500/30 flex items-center justify-center mb-8 group-hover:border-teal-500 transition-colors duration-500">
              <q-icon :name="service.icon" size="sm" class="text-teal-500" />
            </div>
            <h3 class="text-2xl font-serif font-light text-white mb-4">{{ service.name }}</h3>
            <p class="text-white/60 font-sans font-light text-sm leading-relaxed">{{ service.desc }}</p>
            <div class="mt-8 flex items-center gap-3 text-teal-500 text-[10px] uppercase tracking-[0.3em] font-bold font-sans opacity-0 group-hover:opacity-100 transition-opacity duration-500">
              <div class="w-4 h-[1px] bg-teal-500"></div>
              Available On Request
            </div>
          </div>
        </div>
      </div>
    </section>

  </q-page>
</template>

<script setup>
const services = [
  {
    name: 'Helicopter Charters',
    icon: 'flight',
    desc: 'Private helicopter transfers between any two points on the island. Panoramic aerial views over Sigiriya, the Hill Country, and the coastline in under an hour.'
  },
  {
    name: 'Private Jets',
    icon: 'airline_seat_flat',
    desc: 'International private jet arrivals into Bandaranaike International or Ratmalana domestic airport, with ground-to-villa chauffeur transfers arranged bespokely.'
  },
  {
    name: 'Bespoke Air Tours',
    icon: 'panorama',
    desc: 'Scenic aerial photography tours and sunrise helicopter rides over Sri Lanka\'s most breathtaking landscapes — crafted entirely around your schedule and wishes.'
  }
]
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;600;700&display=swap');
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
