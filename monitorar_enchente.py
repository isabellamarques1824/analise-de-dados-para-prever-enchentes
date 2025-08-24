"""
Giovanna da Silva Santos RM566301
Isabella Jardim Marques RM566470
"""



#funcoes

# essa função força o usuario a escrever apenas os valores dentro das opções
def forcar_usuario(mensagem, lista):
      escolha = input(mensagem)
      if not escolha in lista:
            escolha = forcar_usuario(mensagem, lista)
      return escolha

#essa função obriga o usuario a digitar apenas números
def forcar_numero(mensagem):
      n = input(mensagem)
      while not n.isnumeric():
            n = input('Por favor, digite um valor válido: ')
      n = int(n)
      return n

#essa função pergunta se o usuario deseja sair do sistema
def deseja_sair():
    resposta = input("Deseja sair do sistema? (s/n): ").lower()
    if resposta == 's':
        print('Encerrando... Obrigado por utilizar o sistema da HydroSafe Tech.\n'
              'Seguimos juntos pela segurança e prevenção! Até a próxima análise. ')
        return True
    else:
        return False

#essa função analisa o risco de enchentes baseado nos dados inseridos pelo usuario
def analisar_risco(chuva_, nivel):
    if nivel <= 2 and chuva_ <= 20:
        return 'baixo'
    elif nivel <= 4 and chuva_ <= 50:
        return 'moderado'
    else:
        return 'crítico'

# listas onde os dados ficam armazenados

nivel_rio = ['1', '3', '5']
chuva = ['12', '45', '55']
risco = ['baixo', 'moderado', 'crítico']
data = ['30/06/17', '12/07/17', '23/08/17']

#introdução
print('\nHydroSafe Tech - Sistema de Análise de Risco de Enchentes \n'
      'Bem-vindo ao sistema de monitoramento e análise de riscos desenvolvido pela HydroSafe Tech.\n'
      'Versão: 1.0\n'
      'Desenvolvido por: HydroSafe Tech\n')


#menu
while True:
      print('[1] Inserir e analisar novos dados\n'
            '[2] Visualizar dados anteriores\n'
            '[3] Sair\n')

      # escolha

      opcoes = ['1', '2', '3']

      opcao_escolhida = forcar_usuario('Escolha uma opção: ', opcoes)

      # Inserir e analisar novos dados
      if opcao_escolhida == '1':
            data_input = input('Digite a data dos dados que voce quer inserir (digite nesse formato: dd/mm/aa):')
            data.append(data_input)
            chuva_input = forcar_numero('Quando milímetros (mm) de chuva foram registrados nas ultimas 24 horas? ')
            chuva.append(chuva_input)
            rio_input = forcar_numero('Digite a altura do rio registrada (em metros): ')
            nivel_rio.append(rio_input)


            risco_nivel = analisar_risco(chuva_input, rio_input)
            risco.append(risco_nivel)

            # mostrar o nivel de risco baseado na analise feita acima

            if risco_nivel == 'baixo':
                  print(f'data: {data_input} | chuva: {chuva_input}mm | nível do rio: {rio_input}m\n'
                        f'✅ Nível de risco: Baixo \n'
                        f'Situação estável. Nenhum risco de enchente identificado no momento.')
            elif risco_nivel == 'moderado':
                  print(f'data: {data_input} | chuva: {chuva_input}mm | nível do rio: {rio_input}m\n'
                        f'⚠️ Nível de risco: Moderado \n '
                        f'Atenção! Há indícios de possíveis alagamentos. Monitoramento contínuo é recomendado.')
            else:
                  print(f'data: {data_input} | chuva: {chuva_input}mm | nível do rio: {rio_input}m\n'
                        f'🚨 Nível de risco: Crítico \n'
                        f'Alerta máximo! Alto risco de enchente. Acione a defesa civil e tome medidas preventivas imediatamente.')


      #visualizar dados antigos
      elif opcao_escolhida == '2':
            op_visualizar = forcar_usuario('\n[1] Visualizar todos os dados \n'
                                           '[2] Buscar dados por data\n'
                                           'Escolha uma opção:\n', ['1','2'])

            # visualizar todos os dados
            if op_visualizar == '1':
                  for i in range(len(data)):
                        print(f'Data: {data[i]} | Chuva: {chuva[i]}mm | Nível do rio: {nivel_rio[i]}m | Risco: {risco[i]}\n')

            # visualizar dados buscando por data
            elif op_visualizar == '2':
                  busca = input('Digite a data que deseja buscar (formato dd/mm/aa): ')
                  if busca in data:
                        i = data.index(busca)
                        print(f"Data: {data[i]} | Chuva: {chuva[i]}mm | Nível do rio: {nivel_rio[i]}m | Risco: {risco[i]}")
                  else:
                        print('❌ Nenhum dado encontrado para essa data.')


      # pergunta se o usuario deseja sair do sistema
      if deseja_sair():
            break