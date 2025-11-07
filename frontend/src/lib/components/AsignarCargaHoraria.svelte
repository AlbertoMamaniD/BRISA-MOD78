<script lang="ts">
  import { createEventDispatcher } from "svelte";

  export let mostrar = false;

  const dispatch = createEventDispatcher<{
    confirmar: {
      materia: string;
      dia: string;
      curso: string;
      paralelo: string;
      horaInicio: string;
      horaFin: string;
    };
    cancelar: void;
  }>();

  let materia = "";
  let dia = "";
  let curso = "";
  let paralelo = "";
  let horaInicio = "08:00";
  let horaFin = "09:00";

  function confirmar() {
    dispatch("confirmar", { materia, dia, curso, paralelo, horaInicio, horaFin });
  }

  function cancelar() {
    dispatch("cancelar");
  }
</script>

{#if mostrar}
  <div class="modal-overlay">
    <div class="modal">
      <div class="modal-header">
        <h3>Asignar Carga Horaria</h3>
        <button class="btn-close" on:click={cancelar}>×</button>
      </div>

      <div class="modal-body">
        <div class="form-group">
          <label>Materia *</label>
          <select bind:value={materia}>
            <option value="">Seleccione una materia</option>
            <option value="matematicas">Matemáticas</option>
            <option value="lenguaje">Lenguaje</option>
            <!-- Agrega más materias según necesites -->
          </select>
        </div>

        <div class="form-group">
          <label>Día *</label>
          <select bind:value={dia}>
            <option value="">Seleccione un día</option>
            <option value="lunes">Lunes</option>
            <option value="martes">Martes</option>
            <option value="miercoles">Miércoles</option>
            <option value="jueves">Jueves</option>
            <option value="viernes">Viernes</option>
          </select>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Curso *</label>
            <select bind:value={curso}>
              <option value="">Curso</option>
              <option value="1">1ro</option>
              <option value="2">2do</option>
              <!-- Agrega más cursos -->
            </select>
          </div>

          <div class="form-group">
            <label>Paralelo *</label>
            <select bind:value={paralelo}>
              <option value="">Paralelo</option>
              <option value="A">A</option>
              <option value="B">B</option>
              <!-- Agrega más paralelos -->
            </select>
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Hora de Inicio: {horaInicio}</label>
            <input type="range" bind:value={horaInicio} min="07:00" max="18:00" step="1:00" />
          </div>

          <div class="form-group">
            <label>Hora de Fin: {horaFin}</label>
            <input type="range" bind:value={horaFin} min="08:00" max="19:00" step="1:00" />
          </div>
        </div>

        <div class="duracion">
          Duración: 1:00 horas
        </div>
      </div>

      <div class="modal-footer">
        <button class="btn-outline" on:click={cancelar}>Cancelar</button>
        <button class="btn-primary" on:click={confirmar}>Confirmar</button>
      </div>
    </div>
  </div>
{/if}

<style>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }

  .modal {
    background: white;
    border-radius: 12px;
    width: 90%;
    max-width: 500px;
    padding: 24px;
  }

  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
  }

  .modal-header h3 {
    margin: 0;
    font-size: 1.25rem;
    color: #1e293b;
  }

  .btn-close {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #64748b;
  }

  .modal-body {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .form-row {
    display: flex;
    gap: 16px;
  }

  .form-row .form-group {
    flex: 1;
  }

  label {
    font-size: 0.9rem;
    color: #475569;
  }

  select, input {
    padding: 8px 12px;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-size: 0.95rem;
  }

  .duracion {
    text-align: center;
    color: #64748b;
    font-size: 0.9rem;
    margin-top: 8px;
  }

  .modal-footer {
    display: flex;
    justify-content: flex-end;
    gap: 12px;
    margin-top: 24px;
  }

  .btn-outline {
    padding: 8px 16px;
    border: 1px solid #e2e8f0;
    background: white;
    border-radius: 8px;
    color: #64748b;
    cursor: pointer;
  }

  .btn-primary {
    padding: 8px 16px;
    background: #00cfe6;
    border: none;
    border-radius: 8px;
    color: white;
    cursor: pointer;
  }
</style>