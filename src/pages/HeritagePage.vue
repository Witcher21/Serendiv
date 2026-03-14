<template>
  <q-page class="bg-[#030303] text-white relative w-full min-h-screen font-serif">

    <!-- Cinematic Video Background -->
    <video autoplay loop muted playsinline class="fixed inset-0 w-full h-full object-cover opacity-40 filter contrast-[1.1] pointer-events-none z-0">
      <source src="https://www.shutterstock.com/shutterstock/videos/3796051381/preview/stock-footage-3796051381.mp4" type="video/mp4" />
    </video>
    <div class="fixed inset-0 bg-gradient-to-b from-[#030303]/80 via-[#030303]/30 to-[#030303]/90 pointer-events-none z-10"></div>

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
          Heritage Journeys — Sacred Civilizations
        </span>
        <h1 class="text-[4rem] sm:text-[5rem] md:text-[7rem] font-medium leading-[1] tracking-tighter drop-shadow-2xl mb-12 animate-fade-in-up" style="animation-delay:0.2s">
          Ancient<br/>
          <span class="italic font-light text-teal-300">Kingdoms.</span>
        </h1>
        <div class="border-l-2 border-teal-500/50 pl-8 max-w-xl animate-fade-in-up" style="animation-delay:0.4s">
          <p class="font-sans font-light text-white/80 text-base md:text-lg leading-[2]">
            Step into 2,500 years of living history. From the cloud-wrapped rock fortress of Sigiriya to the sacred cave temples of Dambulla, our heritage journeys unlock Sri Lanka's most profound cultural mysteries.
          </p>
        </div>
        <div class="mt-16 flex flex-col sm:flex-row gap-6 animate-fade-in-up" style="animation-delay:0.6s">
          <router-link to="/" class="group px-10 py-5 bg-white text-black font-sans uppercase font-bold tracking-[0.3em] text-[11px] hover:bg-teal-500 hover:text-white transition-all duration-500 relative overflow-hidden inline-flex items-center gap-4">
            <span class="relative z-10">Design My Journey</span>
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
          <span class="uppercase tracking-[0.4em] text-[10px] text-teal-400 font-bold">Signature Experiences</span>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-px bg-white/5 border border-white/5 rounded-3xl overflow-hidden">
          <div v-for="site in sites" :key="site.name" class="group bg-[#050505] hover:bg-teal-900/20 transition-all duration-700 relative overflow-hidden">
            <div class="aspect-[4/3] relative overflow-hidden">
              <img :src="site.img" :alt="site.name" class="w-full h-full object-cover filter brightness-75 group-hover:brightness-100 group-hover:scale-105 transition-all duration-700" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div>
              <div class="absolute bottom-6 left-6">
                <div class="text-[9px] uppercase tracking-[0.3em] font-bold text-teal-400 font-sans mb-2">{{ site.tag }}</div>
                <h3 class="text-2xl font-serif font-light text-white">{{ site.name }}</h3>
              </div>
            </div>
            <div class="p-8">
              <p class="text-white/60 font-sans font-light text-sm leading-relaxed">{{ site.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

  </q-page>
</template>

<script setup>
const sites = [
  {
    name: 'Sigiriya',
    tag: 'UNESCO Heritage',
    img: 'https://images.unsplash.com/photo-1734279135115-6d8984e08206?q=80&w=1200&auto=format&fit=crop',
    desc: 'An 8th Wonder of the World. A colossal 5th-century fortress rising from the jungle plain, adorned with exquisite frescoes and surrounded by elaborate water gardens.'
  },
  {
    name: 'Kandy & The Tooth Relic',
    tag: 'Sacred City',
    img: 'https://images.pexels.com/photos/3389817/pexels-photo-3389817.jpeg?auto=compress&cs=tinysrgb&w=1200',
    desc: 'The last royal capital of Sri Lanka, home to the sacred Temple of the Tooth Relic — the most venerated Buddhist shrine in the world.'
  },
  {
    name: 'Dambulla Cave Temples',
    tag: 'Cave Sanctuaries',
    img: 'https://images.pexels.com/photos/2165074/pexels-photo-2165074.jpeg?auto=compress&cs=tinysrgb&w=1200',
    desc: '2,000-year-old cave temples adorned with 153 Buddha statues and 1,500 sqm of ancient murals, carved into a timeless granite monolith.'
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
