<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'

interface Usuario {
  id: number
  nome: string
}

const usuarios = ref<Usuario[]>([])
const carregando = ref(true)
const erro = ref('')

onMounted(async () => {
  try {
    const resposta = await fetch('/api/usuarios/')

    if (!resposta.ok) {
      throw new Error('Não foi possível carregar os usuários.')
    }

    const dados: { usuarios: Usuario[] } = await resposta.json()
    usuarios.value = dados.usuarios
  } catch (error) {
    erro.value = error instanceof Error ? error.message : 'Erro ao carregar os usuários.'
  } finally {
    carregando.value = false
  }
})
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>

      <section class="usuarios">
        <h2>Usuários</h2>
        <p v-if="carregando">Carregando...</p>
        <p v-else-if="erro" class="erro">{{ erro }}</p>
        <p v-else-if="usuarios.length === 0">Nenhum usuário encontrado.</p>
        <ul v-else>
          <li v-for="usuario in usuarios" :key="usuario.id">{{ usuario.nome }}</li>
        </ul>
      </section>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.usuarios {
  margin-top: 1.5rem;
}

.usuarios h2 {
  font-size: 1.25rem;
}

.usuarios ul {
  padding-left: 1.25rem;
}

.erro {
  color: #b42318;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
