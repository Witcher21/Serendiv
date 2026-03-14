<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container class="bg-[#030303]">
      <router-view v-slot="{ Component }">
        <transition name="page-trans" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </q-page-container>
  </q-layout>
</template>

<style>
.page-trans-enter-active,
.page-trans-leave-active {
  transition: opacity 0.8s cubic-bezier(0.65, 0, 0.35, 1), transform 0.8s cubic-bezier(0.65, 0, 0.35, 1);
}
.page-trans-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.98);
}
.page-trans-leave-to {
  opacity: 0;
  transform: translateY(-20px) scale(1.02);
}
</style>
