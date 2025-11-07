<script lang="ts">
  import { Clock } from "lucide-svelte";
  export let profesor: {
    nombre: string;
    materia: string;
    estado: string;
    experiencia: string;
    cargaHoraria: string;
    correo?: string;
    telefono?: string;
    cursos?: string[];
  };
  export let onClick: () => void = () => {};

  $: iniciales = profesor.nombre
    .split(" ")
    .map((n) => n[0])
    .join("")
    .toUpperCase();
</script>

<div class="card" on:click={onClick} role="button" tabindex="0">
  <div class="avatar">{iniciales}</div>

  <div class="content">
    <div class="top">
      <div class="nombre">{profesor.nombre}</div>
      <span class="materia-pill">{profesor.materia}</span>
    </div>

    <div class="curso-row">
      {#if profesor.cursos && profesor.cursos.length}
        {#each profesor.cursos.slice(0, 2) as c}
          <span class="curso-pill">{c}</span>
        {/each}
        {#if profesor.cursos.length > 2}
          <span class="curso-pill">+{profesor.cursos.length - 2}</span>
        {/if}
      {/if}
    </div>

    <hr class="divider" />

    <div class="footer">
      <div class="left">
        <Clock size="16" color="#64748b" />
        <span class="carga">{profesor.cargaHoraria}</span>
      </div>
      <div class="right">
        <span class="estado-pill {profesor.estado === 'Activo' ? 'activo' : 'inactivo'}">
          {profesor.estado}
        </span>
      </div>
    </div>
  </div>
</div>

<style>
  .card {
    display: flex;
    gap: 18px;
    align-items: flex-start;
    background: #fff;
    border-radius: 12px;
    padding: 20px 22px;
    border: 1px solid #e6eef6;
    width: 100%;          /* <- ocupar todo el ancho de la celda del grid */
    max-width: none;      /* <- quitar límite que encogía horizontalmente */
    box-sizing: border-box;
    cursor: pointer;
    transition: transform 0.12s ease, box-shadow 0.12s ease;
  }
  .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(30, 40, 80, 0.06);
  }

  .avatar {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: #9aa9ff;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 1.05rem;
    flex: 0 0 56px;
  }

  .content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .top {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .nombre {
    font-size: 1rem;
    font-weight: 600; /* más visible como en el diseño */
    color: #263243;
  }

  .materia-pill {
    background: linear-gradient(180deg, #00cfe6, #00bcd4);
    color: #fff;
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    box-shadow: 0 1px 0 rgba(0, 0, 0, 0.03);
  }

  .curso-row {
    display: flex;
    gap: 8px;
    align-items: center;
    margin-top: 6px;
  }

  .curso-pill {
    font-size: 0.75rem;
    color: #3b82f6;
    border: 1px solid #d0e6ff;
    background: #fff;
    padding: 6px 10px;
    border-radius: 999px;
  }

  .divider {
    border: none;
    height: 1px;
    background: #eef4fa;
    margin: 6px 0;
  }

  .footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    font-size: 0.85rem;
    color: #64748b;
  }

  .left {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #64748b;
  }

  .carga { margin-left: 6px; }

  .estado-pill {
    padding: 6px 10px;
    border-radius: 999px;
    font-weight: 700;
    font-size: 0.8rem;
    border: 1px solid transparent;
  }
  .estado-pill.activo {
    background: #e6fff7;
    color: #00a65a;
    border-color: rgba(0, 166, 90, 0.12);
  }
  .estado-pill.inactivo {
    background: #fff6e6;
    color: #ff9800;
    border-color: rgba(255, 152, 0, 0.12);
  }

  @media (max-width: 600px) {
    .card {
      padding: 14px;
    }
    .avatar {
      width: 48px;
      height: 48px;
    }
    .nombre {
      font-size: 0.95rem;
    }
  }
</style>
