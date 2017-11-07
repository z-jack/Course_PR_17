[b] = xlsread('mix.xlsx',1,'A1��D1628');
x = b(:,1);
y = b(:,2);
c = b(:,3);
data = [x,y];
NUM = 500;%��������
Test = sortrows([x(1:NUM,1),y(1:NUM,1),c(1:NUM,1)],3);%Ϊ���㴦�������������
temp = zeros(23,5);%�����洢�����и������Եľ�ֵ�������ÿ����ĸ���
%����������и������Եľ�ֵ�������ÿ����ĸ���
for i = 1:23
    X = [];
    Y = [];
    count = 0;
    for j = 1:NUM
        if Test(j,3)==i
            X = [X;Test(j,1)];
            Y = [Y;Test(j,2)];
            count = count + 1;
        end
    end
    temp(i,1) = mean(X);
    temp(i,2) = std(X);
    temp(i,3) = mean(Y);
    temp(i,4) = std(Y);
    temp(i,5) = count/NUM;
end
%����Ԥ����
result = [];
for m = 1:1628
    pre = [];
    for n = 1:23
        PX = 1/temp(n,2)*exp(((data(m,1)-temp(n,1))^2)/-2/(temp(n,2)^2));
        PY = 1/temp(n,4)*exp(((data(m,2)-temp(n,3))^2)/-2/(temp(n,4)^2));
        pre = [pre;PX*PY*temp(n,5)*10^8];
    end
    [da,index]=max(pre);
    result = [result;index];
end
xlswrite('mix.xlsx',result,'E1:E1628');
%�鿴��ȷ��
num = 0;
for i = 1:1628
    if result(i)==c(i)
        num = num+1;%��ȷ�ĸ���
    end
end