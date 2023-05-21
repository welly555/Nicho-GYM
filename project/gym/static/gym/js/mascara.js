var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
  },
  spOptions = {
    onKeyPress: function(val, e, field, options) {
        field.mask(SPMaskBehavior.apply({}, arguments), options);
      }
  };
  
  

$(function(){
    
    $('.mask-cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('.mask-telefone').mask(SPMaskBehavior, spOptions);
    $('.mask-date').mask('00/00/0000');
    $('.mask-money').mask('000.000.000.000.000,00', {reverse: true});
});

