<script lang="ts">
  import ProfesorCard from "./components/ProfesorCard.svelte";
  import ProfesorDetalle from "./components/ProfesorDetalle.svelte";
  import NuevoProfesor from "./components/NuevoProfesor.svelte";
  import {
    Home,
    Users,
    BookOpen,
    Layers,
    Bell,
    Search,
    LogOut,
  } from "lucide-svelte";
  import { writable } from "svelte/store";

  // Sidebar
  let abierto = writable(true);
  function toggleSidebar() {
    abierto.update((v) => !v);
  }
  const menuItems = [
    { icon: Home, label: "Dashboard" },
    { icon: Users, label: "Usuarios y Roles" },
    { icon: BookOpen, label: "Estudiantes" },
    { icon: BookOpen, label: "Profesores" },
    { icon: Layers, label: "Cursos" },
    { icon: Layers, label: "Administrativos" },
    { icon: Layers, label: "Retiros Tempranos" },
    { icon: Layers, label: "Incidentes" },
    { icon: Layers, label: "Esquelas" },
    { icon: LogOut, label: "Cerrar Sesión" },
  ];

  // Profesores
  type Profesor = {
    nombre: string;
    materia: string;
    estado: string;
    experiencia: string;
    cargaHoraria: string;
    correo: string;
    telefono: string;
    cursos: string[];
  };

  let profesores: Profesor[] = [
    {
      nombre: "Ana María López",
      materia: "Matemáticas",
      estado: "Activo",
      experiencia: "10 años",
      cargaHoraria: "18 hrs/semana",
      correo: "ana@correo.com",
      telefono: "12345678",
      cursos: ["5to A", "6to B"],
    },
    {
      nombre: "Carlos Mendoza",
      materia: "Ciencias Naturales",
      estado: "Activo",
      experiencia: "8 años",
      cargaHoraria: "20 hrs/semana",
      correo: "carlos@correo.com",
      telefono: "87654321",
      cursos: ["5to B", "6to A"],
    },
    {
      nombre: "Lucía Fernández",
      materia: "Historia",
      estado: "Inactivo",
      experiencia: "5 años",
      cargaHoraria: "15 hrs/semana",
      correo: "lucia@correo.com",
      telefono: "11223344",
      cursos: ["4to A", "4to B"],
    },
    {
      nombre: "Miguel Torres",
      materia: "Lengua y Literatura",
      estado: "Activo",
      experiencia: "12 años",
      cargaHoraria: "22 hrs/semana",
      correo: "miguel@correo.com",
      telefono: "44332211",
      cursos: ["3ro A", "3ro B"],
    },
    {
      nombre: "Sofía Ramírez",
      materia: "Inglés",
      estado: "Activo",
      experiencia: "7 años",
      cargaHoraria: "16 hrs/semana",
      correo: "sofia@gmail.com",
      telefono: "55667788",
      cursos: ["2do A", "2do B"],
    },
  ];

  let profesorSeleccionado: Profesor | null = null;
  let searchQuery = "";
  let mostrarNuevoProfesor = false;

  function seleccionarProfesor(p: Profesor) {
    profesorSeleccionado = p;
  }

  function volverALista() {
    profesorSeleccionado = null;
    searchQuery = "";
  }

  function abrirNuevoProfesor() {
    mostrarNuevoProfesor = true;
  }

  function onSaveProfesor(event: CustomEvent) {
    const nuevoProfesor = event.detail;
    profesores = [...profesores, nuevoProfesor];
    mostrarNuevoProfesor = false;
  }

  function onCancelNuevoProfesor() {
    mostrarNuevoProfesor = false;
  }

  $: profesoresFiltrados = profesores.filter((p) => {
    const query = searchQuery.toLowerCase();
    return (
      p.nombre.toLowerCase().includes(query) ||
      p.materia.toLowerCase().includes(query) ||
      p.cursos.some((c) => c.toLowerCase().includes(query))
    );
  });
</script>

<div class="app">
  <!-- Sidebar -->
  <aside class:abierto={$abierto}>
    <div class="brand">
      <div class="brand-left">
        {#if $abierto}
          <div class="logo-mark">BR</div>
          <div class="brand-text">
            <div class="title">BRISA</div>
            <div class="subtitle">Sistema Escolar</div>
          </div>
        {:else}
          <button class="toggle-btn-collapsed" on:click={toggleSidebar}
            >❯</button
          >
        {/if}
      </div>
      {#if $abierto}
        <button class="toggle-btn" on:click={toggleSidebar}>❮</button>
      {/if}
    </div>

    <nav>
      {#each menuItems as item, i}
        <div 
          class="menu-item {i === 3 ? 'active' : ''}"
          on:click={() => {
            if (item.label === "Cerrar Sesión") {
              // Aquí irá la lógica de cerrar sesión
              console.log("Cerrando sesión...");
            }
          }}
          role="button"
          tabindex="0"
        >
          <item.icon size="18" />
          {#if $abierto}<span class="label">{item.label}</span>{/if}
        </div>
      {/each}
    </nav>

    <div class="nav-spacer"></div>
  </aside>

  <!-- Contenido principal -->
  <div class="main-wrap">
    {#if mostrarNuevoProfesor}
      <NuevoProfesor
        on:save={onSaveProfesor}
        on:cancel={onCancelNuevoProfesor}
      />
    {:else}
      <header class="topbar">
        <div class="controls"></div>

        <div class="top-actions">
          <button class="new-btn" on:click={abrirNuevoProfesor}>
            + Nuevo Profesor
          </button>
          <div class="user">
            <div class="avatar">AM</div>
            <div class="user-info">
              <div class="name">Ana María López</div>
              <div class="role">Administrador</div>
            </div>
          </div>
        </div>
      </header>

      <main class:expanded={$abierto}>
        {#if !profesorSeleccionado}
          <section class="page-header">
            <h1>Profesores y Materias</h1>
            <p>Gestiona la información del cuerpo docente</p>

            <div class="controls">
              <input
                class="filter-search"
                type="text"
                placeholder="Buscar por nombre o materia..."
                bind:value={searchQuery}
              />
              <div class="right-controls">
                <button class="filter-btn">Todas las materias ▾</button>
              </div>
            </div>
          </section>

          <section class="panel">
            <h3>Lista de Profesores</h3>

            <div class="grid-profesores">
              {#each profesoresFiltrados as p}
                <ProfesorCard
                  profesor={p}
                  onClick={() => seleccionarProfesor(p)}
                />
              {/each}
              {#if profesoresFiltrados.length === 0}
                <p>No se encontraron profesores.</p>
              {/if}
            </div>
          </section>
        {:else}
          <ProfesorDetalle profesor={profesorSeleccionado} />
          <button class="volver-btn" on:click={volverALista}
            >← Volver a la lista</button
          >
        {/if}
      </main>
    {/if}
  </div>
</div>

<style>
  :root {
    --nav: #0d2e53;
    --nav-secondary: #07264a;
    --accent: #00cfe6;
    --muted: #e9f0f4;
  }

  /* layout */
  .app {
    display: flex;
    width: 100%;
    height: 100vh;
    font-family: "Poppins", sans-serif;
    background: #f6fafc;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    overflow: hidden;
  }

  /* Sidebar */
  aside {
    background: var(--nav);
    color: #cfeaf4;
    width: 260px;
    display: flex;
    flex-direction: column;
    padding: 16px 12px;
    gap: 14px;
    height: 100vh;
    position: fixed;
    left: 0;
    top: 0;
    z-index: 20;
    transition: all 0.3s ease-in-out;
    box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
  }
  aside:not(.abierto) {
    width: 50px;
    transform: translateX(0);
  }

  .brand {
    display: flex;  
    align-items: center;
    justify-content: space-between;
    gap: 8px;
  }
  .brand-left {
    display: flex;
    align-items: center;
    gap: 10px;
    flex: 1;
  }
  .logo-mark {
    width: 44px;
    height: 44px;
    border-radius: 10px;
    background: var(--accent);
    color: #042;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
  }
  .brand-text .title {
    font-weight: 700;
    color: #e6f7fb;
  }
  .brand-text .subtitle {
    font-size: 0.75rem;
    color: #8fb9c6;
  }

  /* menu */
  nav {
    display: flex;
    flex-direction: column;
    gap: 8px;
    overflow: auto;
    padding-right: 6px;
  }
  .menu-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px;
    border-radius: 10px;
    color: #bcdedf;
    cursor: pointer;
    transition: all 0.2s ease-in-out;
    transform-origin: left;
    user-select: none; /* Previene selección de texto */
  }
  .menu-item:hover {
    transform: translateX(4px);
    background: rgba(255, 255, 255, 0.05);
  }
  .menu-item.active {
    background: var(--accent);
    color: #042;
    box-shadow: 0 4px 12px rgba(2, 22, 30, 0.15);
    animation: pulseActive 2s infinite;
  }
  .menu-item .label {
    font-weight: 500;
  }

  /* logout bottom */
  .nav-spacer {
    margin-top: auto;
    padding: 10px 6px;
  }

  /* main content + topbar */
  .main-wrap {
    flex: 1;
    display: flex;
    flex-direction: column;
    margin-left: 260px;
    transition: all 0.3s ease-in-out;
    min-height: 100vh;
    background: #f6fafc;
  }
  aside:not(.abierto) + .main-wrap {
    margin-left: 90px;
  }

  .topbar {
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 28px;
    background: #f6fafc;
    border-bottom: 1px solid #eef6f9;
    position: fixed;
    top: 0;
    right: 0;
    left: 260px;
    z-index: 10;
    transition: all 0.3s ease-in-out;
  }
  aside:not(.abierto) ~ .main-wrap .topbar {
    left: 90px;
  }

  .search {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #fff;
    padding: 8px 12px;
    border-radius: 12px;
    width: 640px;
    box-shadow: 0 2px 6px rgba(20, 40, 60, 0.03);
  }
  .search input {
    border: none;
    outline: none;
    min-width: 300px;
  }
  .top-actions {
    display: flex;
    align-items: center;
    gap: 16px;
  }
  .new-btn {
    background: var(--accent);
    color: #fff;
    border: none;
    padding: 10px 14px;
    border-radius: 10px;
    cursor: pointer;
    font-weight: 600;
  }
  .user {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .user .avatar {
    width: 40px;
    height: 40px;
    border-radius: 999px;
    background: #9aa9ff;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
  }
  .user-info .name {
    font-weight: 600;
    color: #1e293b; /* Color oscuro para el nombre */
  }
  .user-info .role {
    font-size: 0.8rem;
    color: #6b7f86; /* Color más visible para el rol */
  }

  /* page header and controls */
  main {
    padding: 96px 36px 24px;
    height: calc(100vh - 72px);
    margin-top: 72px;
    overflow-y: auto;
  }
  .page-header h1 {
    margin: 0;
    font-size: 1.6rem;
    color: #1e293b; /* Color oscuro para el título */
  }
  .page-header p {
    margin: 6px 0 18px 0;
    color: #6b7f86;
  }
  .controls {
    display: flex;
    gap: 12px;
    align-items: center;
    margin-bottom: 18px;
  }
  .filter-search {
    flex: 1;
    padding: 12px 14px;
    border-radius: 12px;
    border: 1px solid #e7eef2;
    background: #fff;
    color: #1e293b; /* Color de texto más oscuro */
    font-size: 0.95rem;
  }

  .filter-search::placeholder {
    color: #94a3b8; /* Color del placeholder más visible */
  }

  .filter-btn {
    padding: 10px 12px;
    border-radius: 10px;
    background: #fff;
    border: 1px solid #e7eef2;
    color: #475569; /* Color de texto más visible */
    cursor: pointer;
  }

  /* Asegurar que los inputs tengan el texto visible */
  input, select {
    color: #1e293b;
  }

  input::placeholder {
    color: #94a3b8;
  }

  /* panel with cards */
  .panel {
    background: #fff;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 6px 18px rgba(25, 40, 60, 0.02);
    border: 1px solid #eef6fa;
  }
  .grid-profesores {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 14px;
  }
  .grid-profesores > * {
    transition: all 0.3s ease-in-out;
  }

  .grid-profesores > *:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(25, 40, 60, 0.05);
  }

  @media (max-width: 1200px) {
    .grid-profesores {
      grid-template-columns: repeat(2, 1fr);
    }

    .search {
      width: 400px;
    }
  }
  @media (max-width: 768px) {
    aside {
      width: 90px;
    }

    .main-wrap {
      margin-left: 90px;
    }

    .topbar {
      left: 90px;
    }

    .brand-text,
    .menu-item .label {
      display: none;
    }

    .grid-profesores {
      grid-template-columns: 1fr;
    }

    .search {
      width: 100%;
      max-width: 300px;
    }

    .top-actions {
      gap: 8px;
    }

    .user-info {
      display: none;
    }
  }

  /* volver button */
  .volver-btn {
    margin-top: 18px;
    padding: 10px 14px;
    border-radius: 10px;
    border: none;
    background: #00bcd4;
    color: #fff;
  }

  /* small adjustments */
  .toggle-btn {
    background: none;
    border: none;
    color: #cfeaf4;
    cursor: pointer;
    font-size: 18px;
  }
  .toggle-btn-collapsed {
    background: none;
    border: none;
    color: #cfeaf4;
    cursor: pointer;
    font-size: 18px;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease-in-out;
  }

  .toggle-btn-collapsed:hover {
    color: var(--accent);
    transform: translateX(2px);
  }

  @keyframes pulseActive {
    0% {
      box-shadow: 0 0 0 0 rgba(0, 207, 230, 0.4);
    }
    70% {
      box-shadow: 0 0 0 10px rgba(0, 207, 230, 0);
    }
    100% {
      box-shadow: 0 0 0 0 rgba(0, 207, 230, 0);
    }
  }
</style>
