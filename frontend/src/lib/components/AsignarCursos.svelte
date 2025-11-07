<script lang="ts">
  import { createEventDispatcher } from "svelte";
  
  export let idProfesor: number;
  const API_URL = 'http://localhost:8000/api/profesores';
  const dispatch = createEventDispatcher();

  let cursos = [];
  let materias = [];
  let asignacionesPendientes = [];
  let asignacion = {
    id_curso: "",
    id_materia: ""
  };

  async function cargarDatos() {
    try {
      const [resCursos, resMaterias] = await Promise.all([
        fetch(`${API_URL}/cursos`),
        fetch(`${API_URL}/materias`)
      ]);

      cursos = await resCursos.json();
      materias = await resMaterias.json();
    } catch (error) {
      console.error('Error:', error);
    }
  }

  function agregarAsignacion() {
    if (!asignacion.id_materia || !asignacion.id_curso) {
      alert('Seleccione materia y curso');
      return;
    }

    // Encontrar los nombres para mostrar
    const materia = materias.find(m => m.id_materia == asignacion.id_materia);
    const curso = cursos.find(c => c.id_curso == asignacion.id_curso);

    const nuevaAsignacion = {
      ...asignacion,
      nombre_materia: materia?.nombre_materia,
      nombre_curso: curso?.nombre_curso
    };

    // Agregar a la lista local y notificar al padre
    asignacionesPendientes = [...asignacionesPendientes, nuevaAsignacion];
    dispatch('asignado', nuevaAsignacion);

    // Limpiar selección
    asignacion.id_curso = "";
    asignacion.id_materia = "";
  }

  $: cargarDatos();
</script>

<div class="asignar-cursos">
  <div class="form-grid">
    <div class="form-group">
      <label>Materia *</label>
      <select bind:value={asignacion.id_materia} class="select-field">
        <option value="">Seleccione una materia</option>
        {#each materias as materia}
          <option value={materia.id_materia}>{materia.nombre_materia}</option>
        {/each}
      </select>
    </div>

    <div class="form-group">
      <label>Curso *</label>
      <select bind:value={asignacion.id_curso} class="select-field">
        <option value="">Seleccione un curso</option>
        {#each cursos as curso}
          <option value={curso.id_curso}>{curso.nombre_curso} - {curso.gestion}</option>
        {/each}
      </select>
    </div>
  </div>

  <div class="form-actions">
    <button 
      class="btn-primary"
      disabled={!asignacion.id_materia || !asignacion.id_curso}
      on:click={agregarAsignacion}
    >
      Agregar Asignación
    </button>
  </div>

  <!-- Lista de asignaciones pendientes -->
  {#if asignacionesPendientes.length > 0}
    <div class="asignaciones-list">
      <h4>Asignaciones Pendientes</h4>
      <div class="asignaciones-grid">
        {#each asignacionesPendientes as asig}
          <div class="asignacion-card">
            <div class="materia">{asig.nombre_materia}</div>
            <div class="curso">{asig.nombre_curso}</div>
          </div>
        {/each}
      </div>
    </div>
  {/if}
</div>

<style>
  .asignar-cursos {
    background: #fafbfc;
    border-radius: 8px;
    padding: 20px;
    border: 1px solid #e2e8f0;
    margin-top: 20px;
  }

  h3 {
    margin: 0 0 20px;
    font-size: 1rem;
    color: #1e293b;
  }

  .form-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  label {
    font-size: 0.875rem;
    color: #475569;
    font-weight: 500;
  }

  .select-field {
    padding: 0.5rem;
    border: 1px solid #e2e8f0;
    border-radius: 0.375rem;
    background-color: white;
    color: #1e293b;
    width: 100%;
  }

  .select-field option {
    color: #1e293b;
    background: white;
    padding: 0.5rem;
  }

  .form-actions {
    grid-column: span 2;
    display: flex;
    justify-content: flex-end;
    margin-top: 10px;
  }

  .btn-primary {
    padding: 8px 16px;
    background: #00cfe6;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }

  .btn-primary:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .asignaciones-list {
    margin-top: 20px;
  }

  .asignaciones-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
    margin-top: 12px;
  }

  .asignacion-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 12px;
  }

  .materia {
    font-weight: 500;
    color: #1e293b;
  }

  .curso {
    color: #64748b;
    font-size: 0.875rem;
    margin-top: 4px;
  }

  h4 {
    color: #1e293b;
    font-size: 0.95rem;
    margin: 0;
  }

  @media (max-width: 640px) {
    .form-grid {
      grid-template-columns: 1fr;
    }
    .form-actions {
      grid-column: 1;
    }
  }
</style>
