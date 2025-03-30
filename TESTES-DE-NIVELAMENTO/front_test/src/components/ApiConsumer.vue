<template>
  <v-container class="fill-height d-flex flex-column justify-center align-center">
    
    <v-card class="pa-4" width="500">
      <v-card-title class="text-center">Buscar Demonstrações Contábeis</v-card-title>
      <v-card-text>
        <v-text-field 
          v-model="descricao"  
          outlined 
          dense
        ></v-text-field>
        <v-text-field 
          v-model="data" 
          label="Data" 
          type="date" 
          outlined 
          dense
        ></v-text-field>
        <v-btn 
          @click="fetchData" 
          color="primary" 
          block
          class="mt-3"
        >
          Buscar por descrição
        </v-btn>
        <v-btn 
          @click="fetchDataDesc" 
          color="secondary" 
          block
          class="mt-3">
          Buscar por data e descrição
        </v-btn>
        <v-btn 
          @click="fetchDataRegAns" 
          color="tertiary" 
          block
          class="mt-3">
          Buscar por reg_ans
        </v-btn>
      </v-card-text>
    </v-card>

   
    <v-progress-circular v-if="loading" indeterminate color="primary" class="mt-5"></v-progress-circular>

   
    

    <v-row
      class="d-flex justify-center align-center"
      justify="center">
      <v-col 
        v-for="(item, index) in dadosPaginados" 
        :key="index" 
        cols="12" md="4" lg="3"
      >
        <v-card class="mx-2 my-2" width="100%" height="200">
          <v-card-title>{{ item.descricao || "Sem título" }}</v-card-title>
          <v-card-subtitle>cd conta contabil: {{ item.cd_conta_contabil || "Sem tipo" }}</v-card-subtitle>
          <v-card-subtitle>Valor Inicial: {{ item.vl_saldo_inicial || "00,00" }}</v-card-subtitle>
          <v-card-text>Valor final: {{ item.vl_saldo_final || "00,00" }}</v-card-text>
          <v-card-text>Data: {{ item.data || "00/00/0000" }}</v-card-text>

        </v-card>
      </v-col>
      
    </v-row>
    
    <v-pagination
        v-model="paginaAtual"
        :length="Math.ceil(data.length / itensPorPagina)"
      >
    </v-pagination>
    <div class="text-center">
      <strong>Página Atual: {{ paginaAtual }}</strong>
    </div>
  </v-container>
</template>

<script>

import axios from "axios";

export default {
  data() {
  return {
    descricao: "",
    data: [],
    paginaAtual: 1,
    itensPorPagina: 3,
    loading: false,
  };
},
computed: {
  dadosPaginados() {
    const start = (this.paginaAtual - 1) * this.itensPorPagina;
    const end = start + this.itensPorPagina;
    return this.data.slice(start, end);
  }
},
  methods: {
    async fetchData() {
      this.loading = true; 
      if (!this.descricao) {
        alert("Digite uma descrição!");
        return;
      }
      
      try {
        const response = await axios.get(`http://127.0.0.1:5000/demonstracoes_contabeis/descricao/${this.descricao}`);
        
        if (response.data.length > 0) {
          this.data = response.data; 
          this.paginaAtual = 1; 
          this.erro = null;
        } else {
          this.erro = "Nenhum resultado encontrado.";
          this.paginaAtual = 1; 
          this.data = [];
        }
        

      } catch (error) {
        console.error("Erro ao buscar dados:", error);
        this.erro = "Erro ao buscar dados da API.";
        this.data = [];
      }
      this.loading = false;
    },
    async fetchDataRegAns(){
      this.loading = true; 
      if (!this.descricao) {
        alert("Digite um registro!");
        return;
      }
      try {
        const response = await axios.get(`http://127.0.0.1:5000/demonstracoes_contabeis/reg_ans/${this.descricao}`);
        console.log(this.descricao)
        if (response.data.length > 0 ) {
          this.data = response.data; 
          this.paginaAtual = 1; 
          this.erro = null;
        } else {
          this.erro = "Nenhum resultado encontrado.";
          this.paginaAtual = 1; 
          this.data = [];
        }

      } catch (error) {
        console.error("Erro ao buscar dados:", error);
        this.erro = "Erro ao buscar dados da API.";
        this.data = [];
      } 
      this.loading = false;
    },
    async fetchDataDesc(){
      this.loading = true; 
      if (!this.descricao) {
        alert("Digite uma descrição!");
        return;
      }
      try {
        const response = await axios.get(`http://127.0.0.1:5000/demonstracoes_contabeis/relevance/${this.data}/${this.descricao}`);
        
        if (response.data.length > 0 ) {
          this.data = response.data; 
          this.paginaAtual = 1; 
          this.erro = null;
        } else {
          this.erro = "Nenhum resultado encontrado.";
          this.paginaAtual = 1; 
          this.data = [];
        }

      } catch (error) {
        console.error("Erro ao buscar dados:", error);
        this.erro = "Erro ao buscar dados da API.";
        this.data = [];
      }
      this.loading = false;
    }
  }
};
</script>

<style scoped>
.v-card {
  border-radius: 12px;
  background-color: #f8f9fa;
}
</style>
