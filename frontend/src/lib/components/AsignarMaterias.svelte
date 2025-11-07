<script lang="ts">
  import { createEventDispatcher } from "svelte";

  export let idProfesor: number;
  export let asignacionesActuales: any[] = [];

  const API_URL = 'http://localhost:8000/api/profesores';
  const dispatch = createEventDispatcher();

  let materias = [];
  let asignacionesProfesor = [];

  async function cargarDatos() {
    try {
      // Cargar materias disponibles
      const resMaterias = await fetch(`${API_URL}/materias`);
      if (!resMaterias.ok) throw new Error('Error cargando materias');
      materias = await resMaterias.json();

      // Cargar asignaciones del profesor
      const resAsignaciones = await fetch(`${API_URL}/asignaciones/${idProfesor}`);
      if (!resAsignaciones.ok) throw new Error('Error cargando asignaciones');
      asignacionesProfesor = await resAsignaciones.json();
    } catch (error) {
      console.error('Error:', error);
    }
  }

  $: cargarDatos();
</script>

<section class="asignaciones-actuales">
  <h3>Materias Asignadas</h3>
  
  {#if asignacionesProfesor.length > 0}
    <div class="asignaciones-grid">
      {#each asignacionesProfesor as asignacion}
        <div class="asignacion-card">
          <div class="materia">{asignacion.nombre_materia}</div>
          <div class="curso">{asignacion.nombre_curso}</div>
        </div>
      {/each}
    </div>
  {:else}
    <div class="empty-state">
      No hay materias asignadas
    </div>
  {/if}
</section>

<style>
  .asignaciones-actuales {
    margin-top: 20px;
  }

  h3 {
    margin: 0 0 16px;
    font-size: 1rem;
    color: #1e293b;
  }

  .asignaciones-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
  }

  .asignacion-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px;
  }

  .materia {
    font-weight: 500;
    color: #1e293b;
  }

  .curso {
    font-size: 0.875rem;
    color: #64748b;
    margin-top: 4px;
  }

  .empty-state {
    text-align: center;
    color: #64748b;
    padding: 24px;
    background: #f8fafc;
    border-radius: 8px;
    border: 1px dashed #e2e8f0;
  }
</style>
