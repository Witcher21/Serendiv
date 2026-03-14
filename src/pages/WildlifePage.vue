<template>
  <q-page class="bg-[#030303] text-white relative w-full min-h-screen font-serif">

    <!-- Cinematic Video Background -->
    <video autoplay loop muted playsinline class="fixed inset-0 w-full h-full object-cover opacity-40 filter contrast-[1.2] pointer-events-none z-0">
      <source src="https://www.shutterstock.com/shutterstock/videos/3800595019/preview/stock-footage-a-powerful-portrait-of-an-asian-male-elephant-roaming-freely-in-miyamina-park-sri-lanka.mp4" type="video/mp4" />
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
          Wildlife Safaris — Kingdom of the Wild
        </span>
        <h1 class="text-[4rem] sm:text-[5rem] md:text-[7rem] font-medium leading-[1] tracking-tighter drop-shadow-2xl mb-12 animate-fade-in-up" style="animation-delay:0.2s">
          Untamed<br/>
          <span class="italic font-light text-teal-300">Wilderness.</span>
        </h1>
        <div class="border-l-2 border-teal-500/50 pl-8 max-w-xl animate-fade-in-up" style="animation-delay:0.4s">
          <p class="font-sans font-light text-white/80 text-base md:text-lg leading-[2]">
            A raw, uncompromising immersion into the kingdom of the wild. Lock eyes with the elusive Sri Lankan leopard, traverse terrain with nomadic elephants, and witness the grand blue whale migrations off the southern coast.
          </p>
        </div>
        <div class="mt-16 flex flex-col sm:flex-row gap-6 animate-fade-in-up" style="animation-delay:0.6s">
          <router-link to="/" class="group px-10 py-5 bg-white text-black font-sans uppercase font-bold tracking-[0.3em] text-[11px] hover:bg-teal-500 hover:text-white transition-all duration-500 relative overflow-hidden inline-flex items-center gap-4">
            <span class="relative z-10">Design My Safari</span>
            <div class="absolute inset-0 bg-teal-600 transform scale-x-0 origin-left group-hover:scale-x-100 transition-transform duration-500 ease-out z-0"></div>
          </router-link>
          <router-link to="/" class="px-10 py-5 border border-white/30 text-white font-sans uppercase font-bold tracking-[0.3em] text-[11px] hover:border-teal-500 hover:text-teal-400 transition-all duration-500 inline-flex items-center gap-4">
            View All Destinations
          </router-link>
        </div>
      </div>
    </section>

    <!-- Highlights Section -->
    <section class="relative z-20 py-32 px-6 md:px-16 bg-[#030303]/80 backdrop-blur-sm">
      <div class="max-w-[1400px] mx-auto">
        <div class="flex items-center gap-6 mb-20 font-sans">
          <div class="w-12 h-[1px] bg-teal-500"></div>
          <span class="uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold">Safari Portfolio</span>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-px bg-white/5 border border-white/5 rounded-3xl overflow-hidden">
          <div v-for="park in parks" :key="park.name" class="group bg-[#050505] hover:bg-teal-900/20 transition-all duration-700 relative overflow-hidden">
            <div class="aspect-[4/3] relative overflow-hidden">
              <img :src="park.img" :alt="park.name" class="w-full h-full object-cover filter brightness-75 group-hover:brightness-100 group-hover:scale-105 transition-all duration-700" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>
              <div class="absolute bottom-6 left-6">
                <div class="text-[9px] uppercase tracking-[0.3em] font-bold text-teal-400 font-sans mb-2">{{ park.tag }}</div>
                <h3 class="text-2xl font-serif font-light text-white">{{ park.name }}</h3>
              </div>
            </div>
            <div class="p-8">
              <p class="text-white/60 font-sans font-light text-sm leading-relaxed">{{ park.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

  </q-page>
</template>

<script setup>
const parks = [
  {
    name: 'Yala National Park',
    tag: 'Leopard Capital',
    img: 'https://images.unsplash.com/photo-1617867644194-550af3ae2c56?q=80&w=1200&auto=format&fit=crop',
    desc: 'The highest density of leopards in the world. Exclusive jeep safaris at golden hour through Yala\'s dramatic landscape of lagoons, rocky outcrops, and open plains.'
  },
  {
    name: 'Minneriya',
    tag: 'Elephant Gathering',
    img: 'https://images.pexels.com/photos/1598377/pexels-photo-1598377.jpeg?auto=compress&cs=tinysrgb&w=1200',
    desc: 'Witness The Gathering — hundreds of wild Asian elephants converging on the Minneriya tank shores in one of nature\'s most breathtaking spectacles.'
  },
  {
    name: 'Mirissa Whale Watch',
    tag: 'Ocean Giants',
    img: 'https://images.pexels.com/photos/2444403/pexels-photo-2444403.jpeg?auto=compress&cs=tinysrgb&w=1200',
    desc: 'Private catamaran expeditions at dawn to witness the majestic Blue Whale — the largest creature ever to have lived on Earth — in their natural, open ocean habitat.'
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
